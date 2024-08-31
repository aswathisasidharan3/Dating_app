from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.forms import AuthenticationForm


class UserCreationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length=25,
        min_length=8,
        widget=forms.PasswordInput({'class':'form-control'}))
    
    password = forms.CharField(
        max_length=25,
        min_length=8,
        widget=forms.PasswordInput({'class':'form-control'})
    
    )
    phone_number = forms.CharField(
        max_length=10,
        required=True,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number (up to 10 digits)')]
    )

    email = forms.EmailField(
        max_length=254, 
        required=True,
        widget=forms.EmailInput({'class':'form-control'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('Email must be from gmail.com domain.')
        return email
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']



    # otp = forms.CharField(
    #     max_length=6,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter OTP'})
    # )    

class EmailOrMobileAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Email or Mobile', max_length=254,  widget=forms.TextInput({'class':'form-control'}))
    password = forms.CharField(
        max_length=25,
        min_length=8,
        widget=forms.PasswordInput({'class':'form-control'})
    
    )
# class OTPForm(forms.ModelForm):
#     otp = forms.CharField(max_length=6, required=True, label="OTP")