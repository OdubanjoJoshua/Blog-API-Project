from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'body', 'author']
    list_display_links = ['title']
    search_fields = ('title', 'body')
    ordering = ['id',]



admin.site.register(Post, PostAdmin)