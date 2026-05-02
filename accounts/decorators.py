from functools import wraps
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages

def seller_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        if not request.user.profile.seller.is_approved:
            messages.error(request, "Доступ к кабинету продавца пока закрыт: проверка аккаунта еще не пройдена.")
            return redirect('accounts:profile')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def anonymus_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('accounts:profile')
        return view_func(request, *args, **kwargs)
    return _wrapped_view