from django.db import models
from django.utils import timezone

class post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    content = models.TextField()
    email = models.EmailField( blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10)
    imaje = models.ImageField(upload_to='amir/',default='amir/default.jpg')

    def __str__(self):
        return self.title

    


# Create your models here.
