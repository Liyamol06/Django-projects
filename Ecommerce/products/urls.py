from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('product_list', views.Products, name="list_products"),
    path('product_detail', views.DetailedProduct, name="product_detail"),
]