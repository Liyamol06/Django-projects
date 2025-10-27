from django.shortcuts import render

# Create your views here.
def ShowOrders(request):
    return render(request, 'order.html')
