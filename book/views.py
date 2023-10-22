from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms


def book_view(request):
    book_data = models.Book.objects.all()
    return render(request, 'book.html', {'book_key': book_data})


def book_detail_view(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'book_key': book_id})


def create_book_review(request):
    method = request.method
    if method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('your review is successfully added!')
    else:
        form = forms.ReviewForm()

    return render(request, 'create_review.html', {'form': form})


def create_book_view(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('book is successfully added!')
    else:
        form = forms.BookForm()

    return render(request, 'create_book.html', {'form': form})


def book_delete_view(request):
    book_value = models.Book.objects.all()
    return render(request, 'book_list.html', {'book_key': book_value})


def book_drop_view(request, id):
    lang_id = get_object_or_404(models.Book, id=id)
    lang_id.delete()
    return HttpResponse('Successfully deleted')
