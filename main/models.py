from django.db import models


class Slider(models.Model):
    image = models.ImageField('Зображення',
                              upload_to='img',
                              null=True,
                              blank=True,
                              help_text='Зображення буде відображатись на слайдері головної сторінки')
    title = models.CharField('Title',
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