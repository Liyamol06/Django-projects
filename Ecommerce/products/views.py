from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator

# Create your views here.
def Index(request):
    featured_products=Products.objects.order_by('priority')[:4]
    latest_products=Products.objects.order_by('-created_at')[:8]
    context={
        'featured_products': featured_products,
        'latest_products': latest_products,
        }
    return render(request, 'index.html', context)

def ListProducts(request):
    page=1
    if request.GET:
        page=request.GET.get('page')
    products_list=Products.objects.order_by('priority')
    paginator=Paginator(products_list, 4)
    products_list=paginator.page(page)
    context={'products': products_list,}
    return render(request, 'products.html', context)

def DetailedProduct(request, pk):
    prod=Products.objects.get(id=pk)
    context={'product': prod}
    return render(request, 'detailed_product.html', context)
