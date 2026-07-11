from django.db.models import Q
from django.shortcuts import get_object_or_404, render

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
    posts = (
        Post.objects.filter(is_active=True)
        .select_related('author')
        .prefetch_related('category')
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
    content = {
        'posts': posts,
        'popular_posts': get_popular_posts(),
        'query': query,
    }
    return render(request, 'blog-home.html', content)


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
    return render(request, 'contact.html')


def elements(request):
    return render(request, 'elements.html')


def test(request):
    posts = Post.objects.all()
    content = {'posts': posts}
    return render(request, 'test.html', content)
