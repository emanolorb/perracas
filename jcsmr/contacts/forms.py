from django import forms

from .models import Contact


class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'phone', 'email', 'message']