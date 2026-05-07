from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class AnonymousRequiredMixin(AccessMixin):
    """
    Кастомный миксин для запрета входа залогигеных пользователей на страницу логина и регистрации
    """
    redirect_url = 'accounts:profile'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)
    
class LoginRequiredMixin(AccessMixin):
    redirect_url = 'accounts:register'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)
    
class SellerRequiredMixin(AccessMixin):
    redirect_url = 'accounts:profile_update'

    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.seller.is_approved:
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)