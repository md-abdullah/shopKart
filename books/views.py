from django.shortcuts import render
from django.views import generic
from django.db import models
from books.models import Book


class BookListView(generic.ListView):
    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(generic.DetailView):
    def get_queryset(self):
        return Book.objects.all()


# def index(request):
#     dbdata = Book.objects.all()
#     context = {"books": dbdata}
#     return render(request, "books/index.html", context)


# def show(request, id):
#     singleBook = Book.objects.get(pk=id)
#     # for book in data:
#     #     if book["id"] == id:
#     #         singleBook = book
#     context = {"book": singleBook}
#     return render(request, "books/show.html", context)
