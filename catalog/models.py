from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение'),
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Category')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
