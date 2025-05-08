from django.contrib import admin
from .models import Drug

admin.site.register(Drug)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'body', 'images')


class BlogInline(admin.TabularInline):
    model = Drug
    exclude = ['created_at']
    extra = 1
