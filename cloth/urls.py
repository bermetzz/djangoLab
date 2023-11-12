from django.urls import path
from . import views

urlpatterns = [
    path('cloth/product_list/', views.ProductListView.as_view(), name='product_list'),
    path('cloth/products/size_s/', views.size_s, name='size_s'),
    path('cloth/products/size_m/', views.size_m, name='size_m'),
    path('cloth/products/size_l/', views.size_l, name='size_l'),
    path('cloth/products/size_xl/', views.size_xl, name='size_xl'),
    path('cloth/create_order/', views.create_order, name='create_order'),
    path('cloth/products_by_tag/<str:tag_name>/', views.products_by_tag, name='tag'),
]