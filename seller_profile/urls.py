from django.urls import path
from .views import CategoryCreateView

app_name = 'seller_profile'

urlpatterns = [
    path('category-create', CategoryCreateView.as_view(), name='category_create')
]
