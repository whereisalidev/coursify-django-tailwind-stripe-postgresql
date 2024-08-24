from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from django.http import JsonResponse
from django.conf import settings
import stripe




def home(request):
    return render(request, 'home.html')

def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses.html', context)

def enrolled_courses(request):
    courses = Course.objects.filter(enrolled=True)
    context = {'courses': courses}
    return render(request, 'enrolled_courses.html', context)

def course_details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {'course': course, 'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY}
    return render(request, 'course_details.html', context)

def course_video(request, slug):
    if request.user.is_authenticated:
        course = get_object_or_404(Course, slug = slug)
        course.enrolled = True
        course.save()
        context = {'course': course}
        return render(request, 'course_video.html', context)
    else: 
        return redirect('login')

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request, slug):
    course = get_object_or_404(Course, slug=slug)
    YOUR_DOMAIN = 'http://127.0.0.1:8000' 
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': course.name,
                },
                'unit_amount': course.price * 100,  
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=YOUR_DOMAIN + f'/course/{course.slug}/payment_success/',
        cancel_url=YOUR_DOMAIN + f'/course/{course.slug}/',
    )
    return JsonResponse({
        'id': checkout_session.id
    })



def payment_success(request, slug):
    course = get_object_or_404(Course, slug=slug)
    course.purchased = True
    course.save()
    return redirect('course_details', slug=course.slug)

def payment_cancel(request, slug):
    return redirect('course_details', slug=slug)


