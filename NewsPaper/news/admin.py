from django.contrib import admin
from .models import Post, PostCategory, Comment, Category, Author


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time', 'author', 'get_category', 'preview')
    list_filter = ('author', 'category__name', 'type', 'create_time')
    search_fields = ('content', 'title')


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Author)


