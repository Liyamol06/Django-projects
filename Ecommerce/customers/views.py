from django.shortcuts import render

# Create your views here.
def ShowAccount(request):
    return render(request, 'account.html')