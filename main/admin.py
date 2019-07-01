from django.contrib import admin


from .models import *

# Register your models here.



class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    inlines = [PhotoInline]

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.photos.create(image=afile)


admin.site.register(Slider)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Partner)
