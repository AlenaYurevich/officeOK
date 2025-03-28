from django.db import models
from django.utils import timezone
from django.urls import reverse


class Section(models.Model):
    name = models.CharField("Название раздела", max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Product(models.Model):
    sections = models.ManyToManyField(Section, blank=True, verbose_name="Разделы", related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    # Основные поля
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    # Новые поля
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Торговая марка')
    items_per_pack = models.PositiveIntegerField('Количество в упаковке', default=1)
    product_type = models.CharField('Тип', max_length=100, blank=True)  # Или отдельная модель Type
    color = models.CharField('Цвет', max_length=50, blank=True)  # Или ManyToMany на модель Color
    article = models.CharField('Артикул', max_length=50, unique=True)  # Уникальный артикул
    size = models.CharField('Размер', max_length=20, blank=True)  # Число или строка (например, "XL")
    composition = models.TextField('Состав', blank=True)
    specifications = models.JSONField('Дополнительные характеристики', default=dict, blank=True)  # JSON для гибкости

    # Даты
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['article'], name='article_idx'),  # Индекс для артикула
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.pk, self.slug])


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'  # Доступ через product.images.all()
    )
    image = models.ImageField(upload_to='static/product_images/%Y/%m/%d')
    description = models.CharField(max_length=200, blank=True)  # Опциональное описание

    def __str__(self):
        return f"Image for {self.product.name}"
