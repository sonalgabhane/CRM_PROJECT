from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email','first_name','last_name','contact_no','referral','country','website')

        class Meta:
            widgets = {
                'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email Address'})
            }


class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email','first_name','last_name','contact_no','type','area')

        class Meta:
            widgets = {
                'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email Address'})
            }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')