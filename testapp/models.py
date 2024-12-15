from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    date_birth = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    published = models.BooleanField(default=True)
    meta_data = models.JSONField(default=dict)
    has_metadata = models.BooleanField(null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
