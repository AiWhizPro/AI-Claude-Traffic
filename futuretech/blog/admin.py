from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'comparison_keyword', 'published', 'created_at')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'comparison_keyword')
    prepopulated_fields = {'slug': ('title',)}
