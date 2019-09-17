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



def contact(request):
    return render(request, 'contact.html')


def projects(request):
    projects = Project.objects.all()

    filter = None
    try:
        filter = request.GET['filter']
    except:
        ...

    if not filter:
        filter = '*'

    ctx = {'projects': projects,
           'filter': filter}

    return render(request, 'projects.html', ctx)


def project_page(request, id):
    project = Project.objects.get(pk=id)
    gallery = Photo.objects.filter(project=project)

    ctx = {
        'project': project,
        'gallery': gallery,
    }

    return render(request, 'project_page.html', ctx)