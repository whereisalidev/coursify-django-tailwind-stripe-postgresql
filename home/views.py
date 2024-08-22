from django.shortcuts import render



def home(request):
    return render(request, 'home.html')



def products(request):
    return render(request, 'products.html')


def product_details(request):
    return render(request, 'product_details.html')
