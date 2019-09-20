from django.shortcuts import render
from .models import *
from django.core.mail import send_mail, BadHeaderError


# Create your views here.

def send_contact(request):
    fname = request.POST.get('first_name', '')
    lname = request.POST.get('last_name', '')
    subject = 'Message from website'
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')
    whatsapp = request.POST.get('whatsapp', '')
    messages = 'Name and Surname: {} {} \nWhatsApp: {}\nFrom: {}\nMessage: \n{}\n\n\n\nSent From dark-render.com'.format(
        fname, lname, whatsapp, from_email, message)
    send_mail(subject, messages, 'noreply@dark-render.com', ['info@dark-render.com'], fail_silently=False)


def index(request):
    slider = Slider.objects.all()

    ctx = {'slider': slider}

    return render(request, 'index.html', ctx)


def about(request):
    partners = Partner.objects.all()

    ctx = {'partners': partners}
    return render(request, 'about.html', ctx)


def contact(request):
    if request.method == 'POST':
        send_contact(request)
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
