from datetime import datetime

from django.db import models
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
    description = models.TextField('Опис',
                                   help_text='Опис проекта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекти'


class Post(models.Model):
    image = models.ImageField('Зображення',
                              upload_to='img/blog',
                              null=True,
                              blank=True)
    title = models.CharField('Заголовок',
                             max_length=225,
                             help_text='Заголовок статті')
    text = models.TextField('Текст',
                            help_text='Текст статті')
    author = models.CharField('Автор',
                              max_length=125,
                              help_text='Автор')
    date = models.DateTimeField('Дата публікації статті',
                                default=datetime.now,
                                blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стаття Блогу'
        verbose_name_plural = 'Статті Блогу'


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


@receiver(post_delete)
def submission_delete(sender, instance, **kwargs):
    try:
        instance.image.delete(False)
    except AttributeError:
        pass
