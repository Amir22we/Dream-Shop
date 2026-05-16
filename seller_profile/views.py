from django.shortcuts import render, redirect
from catalog.models import Category, Product
from .forms import CategoryCreateForm, CategorySelectForm, ProductCreateForm
from catalog.models import Category
from django.views.generic import CreateView, ListView, TemplateView, UpdateView
from accounts.mixins import SellerRequiredMixin
from django.urls import reverse_lazy

class CategoryCreateView(SellerRequiredMixin, TemplateView):
    template_name = 'pages/catalog/category_product_extra_create.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление категорий'
        context['create_form'] = CategoryCreateForm()
        context['select_form'] = CategorySelectForm()
        return context

    def get_success_url(self):
        return reverse_lazy('accounts:seller_profile')
    
    def post(self, request, *args, **kwargs):

        if 'create' in request.POST:
            form = CategoryCreateForm(request.POST)
            if form.is_valid():
                category = form.save()
                request.user.profile.seller.product_category.add(category)

        if 'select' in request.POST:
            form = CategorySelectForm(request.POST)
            if form.is_valid():
                category = form.cleaned_data['category']
                request.user.profile.seller.product_category.add(category)
        
        return redirect(self.get_success_url())
    
class ProductCreateView(SellerRequiredMixin, CreateView):
    template_name = 'pages/catalog/product_create.html'
    form_class = ProductCreateForm
    model = Product
    success_url = reverse_lazy('accounts:seller_profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Добавление товаров для продавца: {self.request.user.profile}'
        return context
    
    def form_valid(self, form):
        form.instance.seller = self.request.user.profile.seller
        return super().form_valid(form)

class ProductsCreatedBySellerView(SellerRequiredMixin, ListView):
    model = Product
    template_name = 'pages/catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Список всех товаров продавца: {self.request.user.profile}'
        page = context['page_obj']
        context['paginator_range'] = page.paginator.get_elided_page_range(page.number)
        context['out_of_stock'] = Product.objects.filter(stock=0)
        context['not_avaible'] = Product.objects.filter(avaible=False)
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(seller=self.request.user.profile.seller)
    