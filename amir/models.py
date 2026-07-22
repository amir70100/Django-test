from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager



class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    content = models.TextField()
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10)
    image = models.ImageField(upload_to='amir/', default='amir/default.jpg')
    category = models.ManyToManyField(Category)
    tags = TaggableManager()

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def snippets(self):
        return self.content[:100] + '...'

    def author_name(self):
        if not self.author:
            return 'Admin'
        return self.author.get_full_name() or self.author.username


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class NewsLetter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email