from django.forms import ModelForm
from django import forms
from apps.cliente.models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
