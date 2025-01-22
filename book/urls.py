from django.urls import path

from book.views import BookApiView

app_name = 'book'

urlpatterns = [
    path('book/', BookApiView.as_view(), name='book-list'),
]
