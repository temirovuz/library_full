from django.shortcuts import render
from rest_framework.generics import ListAPIView

from book.serializers import CreateBookSerializer
from book.models import Book
# Create your views here.

class BookApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = CreateBookSerializer