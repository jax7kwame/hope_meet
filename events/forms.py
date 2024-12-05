from django import forms
from django.forms import ModelForm
from .models import Venue


# venue form creation
'''
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', "image1", 'image2', 'image3', 'type', 'location', 'county', 'address', 'phone', 'email', 'website_url', 'fb_link', 'ig_link', 'x_link', 'description')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter venue name'
                }),
            "image1": forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
            }),
            'image2': forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file'
            }),
            'image3':forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file'
            }),
            'type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter venue type'
                }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter location'}),
            'county': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter county'}),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Postal address'}),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email address'}),
            'website_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Venue website link'}),
            'fb_link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Venue facebook link'}),
            'ig_link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Venue instagram link'}),
            'x_link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Venue X link'
                }),
            'description': forms.Textarea(attrs={'class': 'form-control',
            'placeholder': 'Venue description'}),
        }
'''