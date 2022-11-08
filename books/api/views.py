from django.shortcuts import render
from rest_framework import generics

from .models import Author, Book
from .serializers import *


class AuthorDetailListView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookDetailListView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer