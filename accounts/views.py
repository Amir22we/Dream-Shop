from django.shortcuts import render, redirect
from .models import Profile, Seller
from .forms import UserRegisterForm, UserLoginForm, RegisterSellerForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import View, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from accounts.decorators import seller_required

class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'pages/accounts/register_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Страница регистрации Arcane Shop'
        return context

    def get_success_url(self):
        return reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save()
        profile = user.profile
        profile.avatar = form.cleaned_data.get('avatar')
        profile.bio = form.cleaned_data.get('bio')
        profile.phone = form.cleaned_data.get('phone')
        profile.city = form.cleaned_data.get('city')
        profile.date_of_birth = form.cleaned_data.get('date_of_birth')
        profile.save()
        return redirect(self.get_success_url())

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
    profile, _ = Profile.objects.get_or_create(user=request.user)
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
    seller_profile, _ = Seller.objects.get_or_create(user=request.user.profile)
    return render(request, 'pages/accounts/seller.html', {'seller_profile': seller_profile})



