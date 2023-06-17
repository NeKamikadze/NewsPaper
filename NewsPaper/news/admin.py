from django.contrib import admin
from .models import Post, PostCategory, Comment, Category, Author


admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Author)


