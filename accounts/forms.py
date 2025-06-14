# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email Address",
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'e.g. you@example.com',
            'class': 'form-control'
        })
    )

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'placeholder': 'Choose a username',
            'class': 'form-control'
        }),
        help_text="Only letters, digits, and @/./+/-/_ are allowed."
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter a strong password',
            'class': 'form-control'
        }),
        help_text=(
            "At least 8 characters. Avoid common passwords and all-numeric passwords."
        )
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Re-enter your password',
            'class': 'form-control'
        }),
        strip=False
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
