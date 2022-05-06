from django.urls import path
from . import views


urlpatterns = [
    # home
    path('', views.getRoutes, name='routes'),
    # products
    path('products/', views.getProducts, name='products'),
    # product
    path('products/<str:pk>/', views.getProduct, name='product'),
]

