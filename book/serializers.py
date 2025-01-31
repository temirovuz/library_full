from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import SerializerMethodField

from book.models import Book, Author, Genre, Language


class CreateAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'description']


class CreateGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class CreateLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['lang']


class CreateBookSerializer(serializers.ModelSerializer):
    authors = CreateAuthorSerializer(many=True)
    genres = CreateGenreSerializer(many=True)
    class Meta:
        model = Book
        fields = ['name', 'isbn', 'summary', 'publication_date', 'authors', 'genres', 'language', 'daily_price',
                  'available_copies']

