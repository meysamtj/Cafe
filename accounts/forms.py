from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomerUser
from django import forms


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomerUser
#         fields = ('first_name','last_name','username', 'birth_day', 'email','phone_number','city','address','image')


class UserCreationForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'birth_day', 'city', 'address', 'image', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomerUser
        fields = ('birth_day', 'email','phone_number','city','address','image','user_type')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

