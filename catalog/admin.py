from django.contrib import admin
from .models import Category, Tag, Product
from django_mptt_admin.admin import DjangoMpttAdmin

class SluggedAdmin(admin.ModelAdmin):
    slug_source = 'name'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prepopulated_fields = {'slug': (self.slug_source,)}

@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin, SluggedAdmin):
    list_display = ('name', 'slug', 'image')
    search_fields = ('name',)
    slug_source = 'name'

@admin.register(Tag)
class TagAdmin(SluggedAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    slug_source = 'name'

@admin.register(Product)
class ProductAdmin(SluggedAdmin):
    search_fields = ('name', )
    slug_source = 'name'