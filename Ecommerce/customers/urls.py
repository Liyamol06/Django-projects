from django.urls import path
from . import views

urlpatterns = [
    path('account', views.ShowAccount, name="account"),
    path('logout', views.LogoutCustomer, name="logout"),
]