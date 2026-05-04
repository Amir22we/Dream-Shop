from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile', verbose_name='Пользователь')
    avatar = models.ImageField(upload_to='accounts/', blank=True, default='media/category/Снимок_экрана_2026-03-29_14-53-20.png', verbose_name='ава')
    bio = models.TextField(blank=True, verbose_name='о себе')
    phone = models.CharField(max_length=40, blank=True, verbose_name='телефон')
    city = models.CharField(max_length=100, blank=True, verbose_name='Город пользовталея')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='День рождение пользователя')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    @property
    def is_seller(self):
        return Seller.objects.filter(profile=self).exists
    
class Seller(models.Model):
    profile = models.OneToOneField(to=Profile, on_delete=models.CASCADE, related_name='seller', verbose_name='Продовец')
    product_category = models.CharField(max_length=100, blank=True,  verbose_name='Категория товаров')
    shop_name = models.CharField(max_length=100, blank=True, verbose_name='Название магазина')  
    is_approved = models.BooleanField(null=True, default=False)

    def __str__(self):
        return str(self.profile)
    