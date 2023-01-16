from django.contrib import admin
from .models import Post, PostCategory, Comment, Author, Category


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Author)

