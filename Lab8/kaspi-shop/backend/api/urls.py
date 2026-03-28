from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('products/', views.products_list, name='products-list'),
    path('products/<int:id>/', views.product_detail, name='product-detail'),
    path('categories/', views.categories_list, name='categories-list'),
    path('categories/<int:id>/', views.category_detail, name='category-detail'),
    path('categories/<int:id>/products/', views.category_products, name='category-products'),
]