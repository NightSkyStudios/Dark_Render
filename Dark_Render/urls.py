from django.contrib import admin
from django.urls import path, re_path, include
from main.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('dev/', admin.site.urls),
    re_path(r'^$', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('projects/', projects, name='projects'),
    path('project_page/<id>', project_page, name='project_page'),
    path(r'tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)