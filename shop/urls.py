from django.urls import path

from shop.views.category import category_index
from . import views

urlpatterns = [
    path('products/', views.product_index),
    path('products/query/<query>/', views.product_query),
    path('products/custom/filter', views.product_filter),
    path('products/query/categories/<slug:slug>', views.category_products),
    path('categories/', views.category_index),
    path('categories/<slug:slug>/products/', views.category_products),
]