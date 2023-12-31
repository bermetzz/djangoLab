from django import forms
from . import models


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.BookReview
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'
