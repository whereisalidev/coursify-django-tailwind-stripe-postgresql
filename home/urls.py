from django.urls import path, include
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('product', views.products, name='product'),
    path('product/details', views.product_details, name='product_details')
]


