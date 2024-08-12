from django.contrib import admin
from .models import BlogPost, Author, Comment

# Register your models here.
class CommentInline(admin.StackedInline):
  model = Comment
  extra = 1
class BlogPostAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'published_date')
  list_filter = ('published_date',)
  search_fields = ('title', 'content')
  inlines = [CommentInline]

class AuthorAdmin(admin.ModelAdmin):
  list_display = ('first_name','last_name', 'email')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Author, AuthorAdmin)