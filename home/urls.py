from django.urls import path, include
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('course', views.courses, name='course'),
    path('enrolled_courses', views.enrolled_courses, name='enrolled_courses'),
    path('course/<slug:slug>/', views.course_details, name='course_details'),
    path('course/<slug:slug>/video', views.course_video, name='course_video'),
    path('course/<slug:slug>/create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('course/<slug:slug>/payment_success/', views.payment_success, name='payment_success'),
    path('course/<slug:slug>/payment_cancel/', views.payment_cancel, name='payment_cancel'),
]


