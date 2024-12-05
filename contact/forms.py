from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'telephone', 'title', 'message')
        labels = {
            'name': '',
            'email': '',
            'telephone': '',
            'title': '',
            'message': ''
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control border border-0 bg-light',
                'id': 'name',
                'name': 'name',
                'placeholder': 'name'
                }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control border border-0 bg-light',
                'id': 'email',
                'type': 'email',
                'name': 'email',
                'placeholder': 'email'
            }),
            'telephone': forms.TextInput(attrs={
                'class': 'form-control border border-0 bg-light',
                'type': 'tel',
                'id': 'tel',
                'name': 'tel',
                'placeholder': 'phone number (optional)'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control border border-0 bg-light',
                'type': 'text',
                'id': 'title',
                'name': 'title',
                'placeholder': 'title'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control bg-light text-dark',
                'placeholder': "Leave a message",
                'id': "message",
                "height": "100px"
            })
        }


