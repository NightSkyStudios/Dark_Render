from datetime import datetime
from django.db import models
from tinymce.models import HTMLField
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Slider(models.Model):
    image = models.ImageField('Зображення',
                              upload_to='img',
                              null=True,
                              blank=True,
                              help_text='Зображення буде відображатись на слайдері головної сторінки')
    title = models.CharField('Заголовок',
                             max_length=225,
                             help_text='Тайл для бокса на слайдері')
    description = models.TextField('Опис',
                                   max_length=125,
                                   help_text='Текст для бокса в коробці')
    category = models.CharField('Категорія (Для переходу по посиланнях)',
                                max_length=2,
                                choices=[('IT', 'Interior'),
                                         ('EX', 'Exterior'),
                                         ('FR', 'Furniture')],
                                default='IT')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотографія Слайдеру'
        verbose_name_plural = 'Фотографії Сладеру'


class Project(models.Model):
    image = models.ImageField('Зображення',
                              upload_to='img',
                              null=True,
                              blank=True)
    title = models.CharField('Заголовок',
                             max_length=225,
                             help_text='Заголовок проекта')
    short_description = models.CharField(max_length=128)
    mce_description = HTMLField('Опис',
                                help_text='Опис проекта')
    category = models.CharField(max_length=2,
                                choices=[('IT', 'Interior'),
                                         ('EX', 'Exterior'),
                                         ('FR', 'Furniture')],
                                default='IT')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекти'


class Partner(models.Model):
    name = models.CharField('Назва',
                            max_length=125,
                            help_text='Назва')
    image = models.ImageField('Зображення',
                              upload_to='img/partners',
                              null=True,
                              blank=True)
    link = models.URLField('Посилання',
                           null=True,
                           blank=True,
                           default='#')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнери'


class Photo(models.Model):
    image = models.ImageField('Зображення',
                              upload_to='img',
                              null=True,
                              blank=True,
                              help_text='Зображення буде відображатись на слайдері головної сторінки')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class VR(models.Model):
    image = models.ImageField('Зображення',
                              upload_to='img/vr',
                              null=True,
                              blank=True)
    title = models.CharField('Заголовок',
                             max_length=225,
                             help_text='Заголовок проекта')
    short_description = models.CharField(max_length=128)
    url = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'VR'
        verbose_name_plural = 'VR'


@receiver(post_delete)
def submission_delete(sender, instance, **kwargs):
    try:
        instance.image.delete(False)
    except AttributeError:
        pass
