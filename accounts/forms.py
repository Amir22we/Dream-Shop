from datetime import date

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, Seller
from datetime import date 

class UserRegisterForm(UserCreationForm):
    avatar = forms.ImageField(label='ава', help_text='только фотки')
    bio = forms.CharField(label='инфа о себе', widget=forms.Textarea, help_text='все что угодно')
    phone = forms.CharField(label='номер телефона')
    city = forms.CharField(label='город')
    date_of_birth = forms.DateField(
        label='дата рождения',
        required=False,
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'autocomplete': 'bday',
            },
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'ник',
            'email': 'почта',
        }
        help_texts = {
            'username': 'норм ник токо'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'пароль'
        self.fields['password2'].label = 'повторно пароль'
        self.fields['password1'].help_text = 'токо не qwerty123 пж'
        self.fields['password2'].help_text = 'буду вахуе если ты забыл'
        self.fields['date_of_birth'].widget.attrs['max'] = date.today().isoformat()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Такой email уже существует')
        return email

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'логин'
        self.fields['password'].label = 'пароль'

class RegisterSellerForm(forms.ModelForm):
    product_category = forms.CharField(max_length=100)
    shop_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'юзер епта'
        self.fields['email'].label = 'почту нахуй'
