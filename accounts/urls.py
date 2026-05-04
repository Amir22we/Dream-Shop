from django.urls import path
from .views import UserRegisterView, UserLoginView, SellerRegisterView
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('logout/', views.logout_view ,name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('seller-register/', SellerRegisterView.as_view(), name='seller_register'),
    path('sellers-profile/', views.seller_profile_view, name='seller_profile')
]
