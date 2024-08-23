from django.urls import path, include
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('product', views.products, name='product'),
    path('product/<slug:slug>/', views.product_details, name='product_details'),
    path('product/<slug:slug>/video', views.course_video, name='course_video')
]


