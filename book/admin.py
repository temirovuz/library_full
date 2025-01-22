from django.contrib import admin
from django.contrib.admin import ModelAdmin

from book.models import Author, Book, Genre


# Register your models here.
@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    list_display = ['id', 'name', 'cleaned_name']
    search_fields = ['name', 'cleaned_name']
    search_help_text = "Nom bo'yicha qidirish"


@admin.register(Genre)
class GenreAdmin(ModelAdmin):
    list_display = ['id','name', 'cleaned_name']
    search_fields = ['name', 'cleaned_name']
    search_help_text = "Nom bo'yicha qidirish"


@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display = ['id','name','cleaned_name']
    search_fields = ['name', 'cleaned_name', 'authors', 'genres']
    search_help_text = "Nom, author, genre bo'yicha qidirish"
