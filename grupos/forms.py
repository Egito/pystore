from django import forms
from .fields import GroupedModelChoiceField
from .models import Grupo, Publico

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields="__all__"

class PublicoForm(forms.ModelForm):
    grupo = GroupedModelChoiceField(
        queryset=Grupo.objects.all(), 
        initial = 0,
        choices_groupby='id'
        )

    class Meta:
        model = Publico
        fields = ['grupo','nick','ativo']
        
#    FormActions(
#        Submit('save_changes', 'Save changes', css_class="btn-primary"),
#        Submit('cancel', 'Cancel'),
#    )