from django.urls import path

from amir.views import (
    about,
    blog_home,
    blog_single,
    contact,
    elements,
    index,
    test,
    newsletter,
)

app_name = 'website'

urlpatterns = [
    path('', index, name='index'),
    path('blog_home', blog_home, name='blog-home'),
    path('about', about, name='about'),
    path('blog_single', blog_single, name='blog-single-page'),
    #path('blog_single', tags_single, name='tags-single-page'),
    path('post-<int:pid>', blog_single, name='blog-single'),
    path('contact', contact, name='contact'),
    path('elements', elements, name='elements'),
    path('test', test, name='test'),
    path('newsletter', newsletter, name='newsletter')
]
