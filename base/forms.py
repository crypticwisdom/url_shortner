from django import forms
from base.models import UrlTable
from django.urls import reverse
from django.shortcuts import redirect

class UrlForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'name':'short',
        'type':'url',
        'placeholder':'Enter Your URL ...',
        'id':'url',

    }))


    class Meta:

        model = UrlTable
        exclude = ('uuid', )

