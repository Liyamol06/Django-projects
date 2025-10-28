from django.shortcuts import render
from . models import Products

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def ListProducts(request):
    products_list=Products.objects.all()
    context={
        'products': products_list,
        }
    return render(request, 'products.html', context)

def DetailedProduct(request):
    return render(request, 'detailed_product.html')
