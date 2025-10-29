from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Customers

# Create your views here.
def LogoutCustomer(request):
    logout(request)
    return redirect('account')

def ShowAccount(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            address=request.POST.get('address')
            password=request.POST.get('password')

            # creating user data
            user=User.objects.create_user(
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
            messages.success(request, "Registration Successful")
        except Exception as e:
            messages.error(request, "Duplicate Username or Invalid Inputs")

    if request.POST and 'login' in request.POST:
        context['register']=False
        name=request.POST.get('name')
        password=request.POST.get('password')
        user=authenticate(username=name, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request, 'account.html')