
from django.urls import path
from amir.views import *

app_name = 'website'

urlpatterns = [
    path('', index, name = 'index'),
    path('blog_home', blog_home, name = 'blog-home'),
    path('about', about, name = 'about'),
    path('blog_single', blog_single, name = 'blog-single-page'),
    path('post-<int:pid>', blog_single, name = 'blog-single'),
    path('contact', contact, name = 'contact'),
    path('elements', elements, name = 'elements'),
    path('test', test, name = 'test'),
]
