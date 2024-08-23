from django.shortcuts import render
from .models import Product



def home(request):
    return render(request, 'home.html')



def products(request):
    products = Product.objects.all()
    context = {'product': products}
    return render(request, 'products.html', context)


def product_details(request):
    return render(request, 'product_details.html')
