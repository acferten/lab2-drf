from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Author, Book
from .serializers import *


class AuthorDetailListView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookDetailListView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreateProductView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = Product.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            price=request.data['price']
        )
        headers = self.get_success_headers(serializer.data)
        return Response({"data:": ({"id": post_new.id, "message:": "Product added"})})
