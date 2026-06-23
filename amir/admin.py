from django.contrib import admin
from amir.models import post

# Register your models here.
class postAdmin(admin.ModelAdmin):
    date_hierarchy = "published_at"
    empty_value_display = "-empty-"
    list_display = ["email", "title", "slug", "is_active" ]

admin.site.register(post, postAdmin)

