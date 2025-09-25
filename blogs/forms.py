from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from phonenumber_field.formfields import SplitPhoneNumberField
from .models import CustomUser
from django_countries.widgets import CountrySelectWidget
from django_password_eye.fields import PasswordEye
class CustomUserCreationForm(UserCreationForm):
    password1 = PasswordEye(label='Password')
    password2 = PasswordEye(label='Repeat Password')
    phone_number = SplitPhoneNumberField(required=False, region="QA")
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2", "phone_number", "profile_picture")
        
        
class CustomAuthenticationForm(AuthenticationForm):
    password = PasswordEye(label='Password')
    class Meta:
        model = CustomUser
        fields = ("username")        
        
        
