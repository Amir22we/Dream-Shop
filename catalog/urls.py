from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryView, ChildCategoryView

app_name = 'catalog'

urlpatterns = [
    path('', CategoryView.as_view(), name='category'),       
    path('all/', ProductListView.as_view(), name='product_list'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('<slug:slug>/', ChildCategoryView.as_view(), name='category-child'),
]