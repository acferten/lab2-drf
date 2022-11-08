from django.urls import path
from .views import *

urlpatterns = [
    path('authors/<int:pk>', AuthorDetailListView.as_view()),
    path('books/<int:pk>', BookDetailListView.as_view())
]
