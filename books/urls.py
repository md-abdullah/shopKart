from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path("", views.BookListView.as_view(), name="index"),
    path("<int:pk>", views.BookDetailView.as_view(), name="show")
]
