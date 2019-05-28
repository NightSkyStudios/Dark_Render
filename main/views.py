from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


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
