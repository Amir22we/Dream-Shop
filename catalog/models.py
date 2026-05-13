from django.db import models
from unidecode import unidecode
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
import uuid

class SluggedModel(models.Model):
    """
    Базовый абстрактный класс для генерации слага
    """
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug', blank=True)
    slug_source = 'name'
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(unidecode(getattr(self, self.slug_source)))
            slug = base_slug
            n = 1
            while self.__class__.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{n}'
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Category(MPTTModel, SluggedModel):
    """
    Модель категорий 
    """
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(max_length=300, verbose_name='Описание', default='Описание отсутсвует')
    image = models.ImageField(upload_to='category/', blank=True, verbose_name='Изображение')
    parent = TreeForeignKey(
        to='self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Родительская категория',
        related_name='children'
    )
    class MPTTMeta:
        order_insertion_by = ('name',)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("catalog:category-child", kwargs={"slug": self.slug})
    

class Tag(SluggedModel):
    """
    Модель тегов к модели продуктов
    """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
    

class Product(SluggedModel):
    """
    Модель продуктов
    """
    # id = models.AutoField(verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name='Название')
    category = TreeForeignKey(
        Category, 
        on_delete=models.PROTECT, 
        verbose_name='Категория'
        )
    # tags = TaggableManager(verbose_name='Теги')
    tags = models.ManyToManyField(Tag)
    description = models.TextField(blank=True, max_length=5000, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='Количество на складе')
    avaible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey('accounts.Seller', on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
