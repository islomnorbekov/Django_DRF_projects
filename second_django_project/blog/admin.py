from django.contrib import admin
from .models import Post

admin.site.register(Post)
admin.site.site_header = "Courses Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcome to Courses Admin"


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'body', 'images')


class BlogInline(admin.TabularInline):
    model = Post
    exclude = ['created_at']
    extra = 1
