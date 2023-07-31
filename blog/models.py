from django.db import models

NULLABLE = {'blank': True, 'null': True}


class BlogEntru(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name='slug')
    content = models.TextField(**NULLABLE, verbose_name='содержимое')
    preview = models.ImageField(upload_to='main/', **NULLABLE, verbose_name='превью (изображение)')
    creation_date = models.DateField(**NULLABLE, verbose_name='дата создания')
    publication_attribute = models.BooleanField(default=True, verbose_name='признак публикации')
    number_views = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title} {self.number_views}'

    class Meta:
        verbose_name = 'Блоговая запись'
        verbose_name_plural = 'Блоговые записи'
