from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from amir.forms import NameForm, ContactForm, PostForm, NewsLetterForm
from amir.models import Post


def get_popular_posts():
    return (
        Post.objects.filter(is_active=True)
        .select_related('author')
        .order_by('-published_at')[:3]
    )


def index(request):
    return render(request, 'index.html')


def blog_home(request):
    query = request.GET.get('q', '').strip()
    tag_name = request.GET.get('tag', '').strip()
    posts = (
        Post.objects.filter(is_active=True)
        .select_related('author')
        .prefetch_related('category', 'tags')
        .order_by('-published_at')
    )
    if query:
        posts = posts.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(category__name__icontains=query)
            | Q(author__username__icontains=query)
            | Q(author__first_name__icontains=query)
            | Q(author__last_name__icontains=query)
        ).distinct()

    if tag_name:
        posts = posts.filter(tags__name__iexact=tag_name)

    paginator = Paginator(posts, 3)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'posts': page_obj,
        'page_obj': page_obj,
        'popular_posts': get_popular_posts(),
        'query': query,
        'tag_name': tag_name,
    }
    return render(request, 'blog-home.html', context)


def about(request):
    return render(request, 'about.html')


def blog_single(request, pid=None):
    selected_post = None
    if pid is not None:
        selected_post = get_object_or_404(
            Post.objects.select_related('author').prefetch_related('category'),
            id=pid,
            is_active=True,
        )
    return render(request, 'blog-single.html', {
        'post': selected_post,
        'popular_posts': get_popular_posts(),
    })


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('website:contact')
        else:
            messages.error(request, 'There was an error sending your message. Please check the fields.')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {"form": form})
    


def elements(request):
    return render(request, 'elements.html')


def test(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("done")

    else:
        form = PostForm()

    return render(request, "test.html", {"form": form})

def newsletter(request):
    if request.method == "POST":
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed to our newsletter!')
        else:
            messages.error(request, 'Invalid email address.')
    return redirect('/')