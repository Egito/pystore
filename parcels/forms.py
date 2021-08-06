from django import forms
from .models import Parcela

class ParcelaForm(forms.ModelForm):
    class Meta:
        model = Parcela
        fields="__all__"
