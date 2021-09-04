from django import forms
from .fields import GroupedModelChoiceField
from .models import Radios, TipoOperacao, CapaMov, Movimento

class RadioForm(forms.ModelForm):
    class Meta:
        model = Radios
        fields="__all__"

class TipoForm(forms.ModelForm):
    class Meta:
        model = TipoOperacao
        fields="__all__"

class CapaForm(forms.ModelForm):
    class Meta:
        model = CapaMov
        fields="__all__"

class MovimentoForm(forms.ModelForm):
    Tipo = GroupedModelChoiceField(
        queryset=TipoOperacao.objects.all(), 
        initial = 0,
        choices_groupby='id'
        )
    Capa = GroupedModelChoiceField(
        queryset=CapaMov.objects.all(), 
        initial = 0,
        choices_groupby='id'
        )
    Radio = GroupedModelChoiceField(
        queryset=Radios.objects.all(), 
        initial = 0,
        choices_groupby='id'
        )

    class Meta:
        model = Movimento
        fields = ['capa','radio','tipo','descricao','dado','ativo']
        
#    FormActions(
#        Submit('save_changes', 'Save changes', css_class="btn-primary"),
#        Submit('cancel', 'Cancel'),
#    )