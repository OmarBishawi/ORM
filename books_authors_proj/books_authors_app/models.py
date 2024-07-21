
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

