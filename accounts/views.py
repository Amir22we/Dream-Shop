from django.shortcuts import render
from .models import Profile, Seller
from .forms import UserRegisterForm, UserLoginForm, RegisterSellerForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import View, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from accounts.decorators import seller_required

class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('catalog:category')
    template_name = 'pages/accounts/register_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Страница регистрации Arcane Shop'
        return context

class UserLoginView(LoginView):
    form_class = UserLoginForm
    success_url = reverse_lazy('accounts:register')
    template_name = 'pages/accounts/login_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Страница логина'
        return context
    
@login_required
def profile_view(request):
    profile = Profile.objects.get_or_create(user=request.user)
    return render(request, 'pages/accounts/profile.html', {'profile': profile})

class SellerRegisterView(CreateView):
    form_class = RegisterSellerForm
    success_url = reverse_lazy('catalog:category')
    template_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Страница регистрации продавцов'
        return context

@seller_required
def seller_profile_view(request):
    seller_profile = Seller.objects.get_or_create(user=request.user.profile)
    return render(request, 'pages/accounts/seller.html', {'seller_profile': seller_profile})



