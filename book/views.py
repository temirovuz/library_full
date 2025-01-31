from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from book.permissions import IsAdmin
from book.serializers import CreateBookSerializer, ListBooksSerializer
from book.models import Book


# Create your views here.

class BookApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = ListBooksSerializer

class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = CreateBookSerializer