from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):

    slider = Slider.objects.all()

    ctx = {'slider': slider}

    return render(request, 'index.html', ctx)


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def projects(request):
    return render(request, 'projects.html')


def service(request):
    return render(request, 'service.html')


def blog_post(request):
    return render(request, 'blog-single.html')
