from django.shortcuts import render, get_object_or_404
from .models import Product



def home(request):
    return render(request, 'home.html')



def products(request):
    products = Product.objects.all()
    context = {'product': products}
    return render(request, 'products.html', context)


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'product_details.html', context)
