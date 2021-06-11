from django.db import models
from django.db.models.deletion import CASCADE


class Author(models.Model):
    title = models.CharField(max_length=200)
    now = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Book(models.Model):
    name = models.CharField(max_length=200)
    pageCount = models.IntegerField()
    thumbnailUrl = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return f"{self.id}-{self.name}"


class Review(models.Model):
    title = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=CASCADE)

    def __str__(self):
        return f"{self.book} - {self.title}"
