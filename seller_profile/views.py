from django.shortcuts import render, redirect
from catalog.models import Category
from .forms import CategoryCreateForm
from catalog.models import Category
from django.views.generic import CreateView, ListView
from accounts.mixins import SellerRequiredMixin
from django.urls import reverse_lazy

class CategoryCreateView(SellerRequiredMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'pages/catalog/category_product_extra_create.html'

    def get_object(self, queryset=None):
        return self.request.GET.get('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление категорий'
        return context

    def get_success_url(self):
        return reverse_lazy('accounts:seller_profile')
    
class AllCategoryCreatedBySeller(SellerRequiredMixin, ListView):
    model = Category
    template_name = ''
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context['title'] = 'просмотр категории'
        return context
    