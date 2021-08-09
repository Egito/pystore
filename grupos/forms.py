from django import forms
from .fields import GroupedModelChoiceField
from .models import Grupos, Jogadores

class GruposForm(forms.ModelForm):
    class Meta:
        model = Grupos
        fields="__all__"

class JogadoresForm(forms.ModelForm):
    grupo = GroupedModelChoiceField(
        queryset=Grupos.objects.all(), 
        initial = 0,
        choices_groupby='id'
        )

    class Meta:
        model = Jogadores
        fields = ['grupo','nick','ativo']
        
#    FormActions(
#        Submit('save_changes', 'Save changes', css_class="btn-primary"),
#        Submit('cancel', 'Cancel'),
#    )