from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Tag, Product

class ProductListView(ListView):
    model = Product
    template_name = 'pages/catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 12
    # queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список всех продуктов'
        page = context['page_obj']
        context['paginator_range'] = page.paginator.get_elided_page_range(page.number)
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'pages/catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Товар: {self.object.name}'
        return context

class CategoryView(ListView):
    model = Category
    template_name = 'pages/catalog/category_list.html'
    context_object_name = 'category'
    paginate_by = 12

    def get_queryset(self):
        return Category.objects.filter(parent=None)
    
class ChildCategoryView(ListView):
    model = Category
    template_name = 'pages/catalog/category_child_list.html'
    context_object_name = 'items'

    def get_category(self):
        if not hasattr(self, '_category'):
            self._category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return self._category
    
    def get_queryset(self):
        category = self.get_category()
        if category.get_children().exists():
            return category.get_children()
        else:
            return Product.objects.filter(category=category)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_category()
        context['category'] = category
        context['breadcrumbs'] = category.get_ancestors(include_self=True)
        context['has_children'] = category.get_children().exists()
        return context