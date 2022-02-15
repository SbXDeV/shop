import random
from unicodedata import category

from django.db import models


class Categories(models.Model):
    title = models.CharField(verbose_name='Наименование категории', max_length=100)

    class Meta:
        verbose_name = 'Категории товаров'
        verbose_name_plural = 'Категория товаров'

    def __str__(self):
        return 'Категория: ' + self.title


class Product(models.Model):
    type_choice = (
        (1, 'Для Мальчиков'),
        (2, 'Для Девочек'),
        (3, 'Для Малышей'),
    )
    picture = models.ImageField(upload_to='media/', verbose_name='Фотография продукта')
    namespace = models.CharField(max_length=100, verbose_name='Наименование товара')
    trand = models.BooleanField(verbose_name='Трендовый товар', default=True)
    star = models.IntegerField(verbose_name='Количество звезд')
    price = models.IntegerField(verbose_name='Цена за товар')
    category = models.ManyToManyField(Categories)
    description = models.TextField(verbose_name='Описание товара')
    sku = models.IntegerField(verbose_name='Код товара', default=random.randint(0, 999999))
    gender = models.IntegerField(choices=type_choice, verbose_name='Принадлежность товара')

    class Meta:
        verbose_name = 'Товары сайта'
        verbose_name_plural = 'Товар сайта'

    def __str__(self):
        return 'Товар: ' + self.namespace


class Police(models.Model):
    content = models.TextField(verbose_name='Содержание политики конфиденциальности',
                               help_text='Политику конфиденциальности можно и нужно добавлять один раз!')

    class Meta:
        verbose_name = 'Политика'
        verbose_name_plural = 'Политика'

    def __str__(self):
        return 'Редактировать содержимое'


class Transport(models.Model):
    content = models.TextField(verbose_name='Содержание', help_text='Содержимое поля можно и нужно добавлять один раз!')

    class Meta:
        verbose_name = 'Оплата и доставка'
        verbose_name_plural = 'Оплата и доставка'

    def __str__(self):
        return 'Редактировать содержимое'


class Sale(models.Model):
    picture = models.ImageField(upload_to='media/', verbose_name='Фотография')
    author = models.CharField(verbose_name='Опубликовано', max_length=100, default='Администратор')
    date = models.DateTimeField(verbose_name='время публикации')
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    content = models.TextField(verbose_name='Содержание')

    class Meta:
        verbose_name = 'Акции'
        verbose_name_plural = 'Акция'

    def __str__(self):
        return 'Редактировать содержимое: ' + ' ' + self.title

