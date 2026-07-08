from django.shortcuts import get_object_or_404, render
from amir.models import post

def get_popular_posts():
    return post.objects.filter(is_active=True).order_by('-published_at')[:3]

def index(request):
    return render(request, "index.html")

def blog_home(request):
    posts = post.objects.filter(is_active=True).order_by('-published_at')
    content = {
        'posts': posts,
        'popular_posts': get_popular_posts(),
    }
    return render(request, "blog-home.html", content)

def about(request):
    return render(request, "about.html")

def blog_single(request, pid=None):
    selected_post = None
    if pid is not None:
        selected_post = get_object_or_404(post, id=pid, is_active=True)
    return render(request, "blog-single.html", {
        'post': selected_post,
        'popular_posts': get_popular_posts(),
    })

def contact(request):
    return render(request, "contact.html")

def elements(request):
    return render(request, "elements.html")

def test(request):
    posts = post.objects.all()
    content = {'posts': posts}
    return render(request, "test.html", content)


# Create your views here.
