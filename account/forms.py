from django import forms
from django.contrib.auth.password_validation import validate_password
from .models import Account


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter first name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter last name'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Create username'
    }))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder': 'Enter phone number'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter email',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password'
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'password']
    #check password similarity
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match!")
            
            validate_password(confirm_password)
        
        return super().clean()

