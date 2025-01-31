from django.urls import path

from book.views import BookApiView, BookCreateAPIView

app_name = 'book'

urlpatterns = [
    path('books/', BookApiView.as_view(), name='book-list'),
    path('create/', BookCreateAPIView.as_view(), name='book-create'),
]
