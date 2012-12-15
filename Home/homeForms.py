__author__ = 'Jacob'

from django import forms

class ContactForm(forms.Form):
    Name = forms.CharField(max_length=100)
    Message = forms.CharField()
    Email = forms.EmailField()
