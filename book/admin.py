from django.contrib import admin
from django.contrib.admin import ModelAdmin

from book.models import Author, Book, Genre, Language


# Register your models here.
@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    fields = ['name', 'description']
    readonly_fields = ['cleaned_name']
    list_display = ['id', 'name', 'cleaned_name']
    search_fields = ['name', 'cleaned_name']
    search_help_text = "Nom bo'yicha qidirish"


@admin.register(Genre)
class GenreAdmin(ModelAdmin):
    fields = ['name']
    readonly_fields = ['cleaned_name']
    list_display = ['id', 'name', 'cleaned_name']
    search_fields = ['name', 'cleaned_name']
    search_help_text = "Nom bo'yicha qidirish"


@admin.register(Language)
class LanguageAdmin(ModelAdmin):
    fields = ['lang']
    readonly_fields = ['cleaned_lang']
    list_display = ['id', 'lang', 'cleaned_lang']
    search_fields = ['lang', 'cleaned_lang']
    search_help_text = "Til bo'yicha qidirish"


@admin.register(Book)
class BookAdmin(ModelAdmin):
    fields = ['name', 'isbn', 'summary', 'publication_date', 'authors', 'genres', 'language', 'daily_price',
              'available_copies']
    readonly_fields = ['cleaned_name']
    list_display = ['id', 'name', 'isbn', 'publication_date', 'display_authors', 'display_genres']
    search_fields = ['name', 'cleaned_name', 'authors', 'genres']
    search_help_text = "Nom, author, genre bo'yicha qidirish"
