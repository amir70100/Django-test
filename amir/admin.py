from django.contrib import admin

from amir.models import Category, Post


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_at'
    empty_value_display = '-empty-'
    list_display = ['email', 'title', 'slug', 'author', 'is_active']
    search_fields = [
        'title',
        'content',
        'author__username',
        'author__first_name',
        'author__last_name',
    ]

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
