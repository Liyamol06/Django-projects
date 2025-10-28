from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def ListProducts(request):
    page=1
    if request.GET:
        page=request.GET.get('page')
    products_list=Products.objects.all()
    paginator=Paginator(products_list, 2)
    products_list=paginator.page(page)
    context={'products': products_list,}
    return render(request, 'products.html', context)

def DetailedProduct(request):
    return render(request, 'detailed_product.html')
