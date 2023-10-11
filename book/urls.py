from django.urls import path
from . import views

urlpatterns = [
    # path('main_page_books/', views.book_view),
    path('', views.book_view),
]
