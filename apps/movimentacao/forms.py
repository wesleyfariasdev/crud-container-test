from django import forms
from django.forms import ModelForm
from apps.movimentacao.models import Movement


class MovementForm(ModelForm):
    class Meta:
        model = Movement
        fields = '__all__'
        widgets = {
            'initial_date': forms.DateTimeInput(
                attrs={
                    'type': 'date',
                }
            ),
            'finish_date': forms.DateTimeInput(
                attrs={
                    'type': 'date',
                }
            )
        }
