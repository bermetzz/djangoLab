from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookView.as_view()),
    path('book_detail/<int:id>/', views.BookDetailView.as_view()),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_list/<int:id>/delete/', views.BookDropView.as_view(), name='delete'),
    path('book_list/<int:id>/update/', views.UpdateBookView.as_view(), name='update'),
    path('add-book/', views.CreateBookView.as_view()),
    path('add-review/', views.create_book_review),
    path('search/', views.SearchView.as_view(), name='search'),
]
