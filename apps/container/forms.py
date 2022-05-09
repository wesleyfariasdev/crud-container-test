from django import forms
from django.forms import ModelForm
from apps.container.models import Container


class ContainerForm(ModelForm):
    class Meta:
        model = Container
        fields = '__all__'
