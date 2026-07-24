from django.contrib import admin
from amir.models import Category, Post, Contact, NewsLetter
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
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


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(NewsLetter, NewsLetterAdmin)

