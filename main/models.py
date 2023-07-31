from django.db import models

NULLABLE = {'blank': True, 'null': True}
nl = '\n'


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')

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
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, verbose_name='категория', **NULLABLE)
    publication_attribute = models.BooleanField(default=True)
    number_views = models.IntegerField(default=0, verbose_name=' number_views')

    def __str__(self):
        return f'{self.name} ({self.description}), {self.number_views}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, verbose_name='продукт', **NULLABLE)
    name_version = models.CharField(max_length=150, verbose_name='название версии')
    name_current_version = models.BooleanField(default=True, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.name_version} ({self.name_current_version})'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
