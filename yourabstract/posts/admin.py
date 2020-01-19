from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish', 'author']
    list_filter = ['author', 'publish']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ['author', ]
