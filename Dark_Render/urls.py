from django.contrib import admin
from django.urls import path, re_path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('projects/', projects, name='projects'),
    path('service/', service, name='service'),
    path('blog-post/', blog_post, name='blog_post'),
]
