from django.contrib import admin
from .models import Book, Library, Genre, Review
# Register your models here.
"""Qadam 3: Admin Interfeysini Moslashtirish va Inline Elements
Library modelini admin interfeysiga qo'shing va list_display parametrini name va location bilan moslang.

Genre modelini admin interfeysiga qo'shing.

Book modelini admin interfeysiga qo'shing.

Book modeli uchun Review modelini yarating: book (ForeignKey Book modeliga), review_text (TextField), rating (IntegerField), created_at (DateTimeField).

Review modelini Book modeliga inline sifatida qo'shing (TabularInline).

Admin interfeysida Book modelini moslashtiring: list_display (title, author, published_date, library), list_filter (published_date, genres), search_fields (title, author)."""
class LibraryAdmin(admin.ModelAdmin):
  list_display = ['name', 'location']

class ReviewInline(admin.TabularInline):
  model = Review
  extra = 1

class BookAdmin(admin.ModelAdmin):
  list_display = ['title', 'author', 'published_date', 'library']
  list_filter = ('published_date', 'genres',)
  search_fields = ('title', 'author')
  inlines = [ReviewInline]

admin.site.register(Book, BookAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Genre)