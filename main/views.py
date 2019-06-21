from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    slider = Slider.objects.all()

    ctx = {'slider': slider}

    return render(request, 'index.html', ctx)


def about(request):
    partners = Partner.objects.all()

    ctx = {'partners': partners}
    return render(request, 'about.html', ctx)


def blog(request):
    posts = Post.objects.all().order_by('-date')

    ctx = {'posts': posts}
    return render(request, 'blog.html', ctx)


def contact(request):
    return render(request, 'contact.html')


def projects(request):
    projects = Project.objects.all()

    ctx = {'projects': projects}
    return render(request, 'projects.html', ctx)


def project_page(request, id):
    project = Project.objects.get(pk=id)

    ctx = {'project': project}

    return render(request, 'project_page.html', ctx)


def blog_post(request,id):
    post = Post.objects.get(pk=id)

    ctx = {'post': post}
    return render(request, 'blog-single.html',ctx)
