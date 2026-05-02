from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class AnonymousRequired(AccessMixin):
    """
    Кастомный миксин для запрета входа залогигеных пользователей на страницу логина и регистрации
    """
    redirect_url = 'accounts:profile'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)