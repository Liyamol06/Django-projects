from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def Products(request):
    return render(request, 'products.html')

def DetailedProduct(request):
    return render(request, 'detailed_product.html')
