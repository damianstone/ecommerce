from django.urls import path
from base.views import product_views as views


urlpatterns = [
    # empty cuz in backend urls is api/product/
    path('', views.getProducts, name='products'),
    # product by id
    path('<str:pk>/', views.getProduct, name='product'),
]