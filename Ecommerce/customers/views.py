from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customers

# Create your views here.
def ShowAccount(request):
    if request.POST and 'register' in request.POST:
        print(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        password=request.POST.get('password')

        # creating user data
        user=User.objects.create(
            username=name,
            password=password,
            email=email
        )
        #  creating customer data 
        customer=Customers.objects.create(
            name=name,
            phone=phone,
            address=address,
            email=email,
            user=user
        )
        return redirect('home')
    elif request.POST and 'login' in request.POST:
        print('-------------------------------------------------')
        print('Login form')
        print('-------------------------------------------------')
    return render(request, 'account.html')