from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('product_list', views.ListProducts, name="list_products"),
    path('product_detail/<pk>', views.DetailedProduct, name="product_detail"),
]