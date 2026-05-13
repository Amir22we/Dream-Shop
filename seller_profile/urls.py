from django.urls import path
from .views import CategoryCreateView, ProductCreateView

app_name = 'seller_profile'

urlpatterns = [
    path('category-create', CategoryCreateView.as_view(), name='category_create'),
    path('product-create', ProductCreateView.as_view(), name='product_create')
]
