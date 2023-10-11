from django.shortcuts import render
from . import models


def book_view(request):
    book_data = models.Book.objects.all()
    return render(request, 'book.html', {'book_key': book_data})
