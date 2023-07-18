from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    # created_at = models.CharField(max_length=150, verbose_name='вносимое поле')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    price = models.IntegerField(default=0, verbose_name='цена за покупку')
    photo = models.ImageField(upload_to='main/', **NULLABLE, verbose_name='изображение(превью)')
    birth_day = models.DateField(**NULLABLE, verbose_name='дата создания')
    last_change = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')
    category = models.CharField(max_length=150, verbose_name='категория')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
