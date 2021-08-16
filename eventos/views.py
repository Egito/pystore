from django.shortcuts import render
from openpyxl import load_workbook
from django import forms
import os

from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Evento, SessaoEvento, Publico
from django.urls import reverse_lazy

#---- Create Views ----#

class CreateEvento(CreateView):
    model = Evento
    fields = ['descr']
    template_name = "eventos/form.html"
    success_url = reverse_lazy('eventos:listar-evento')

class CreatePublico(CreateView):
    model = Publico
    fields = ['nick', 'email', 'publico_filho']
    template_name = "eventos/form.html"
    success_url = reverse_lazy('eventos:listar-publico')

class CreateSessaoEvento(CreateView):
    model = SessaoEvento
    fields = ['evento', 'descr', 'regras', 'dataini', 'datafim']
    template_name = "eventos/form.html"
    success_url = reverse_lazy('eventos:listar-sessao-evento')

#---- Atualizar ----#

class UpdateEvento(UpdateView):
    model = Evento
    fields = ['descr', 'ativo']
    template_name = "eventos/form.html"
    success_url = reverse_lazy('eventos:listar-evento')

class UpdatePublico(UpdateView):
    model = Publico
    fields = ['nick', 'email', 'publico_filho', 'ativo']
    template_name = "eventos/form.html"
    success_url = reverse_lazy('eventos:listar-publico')

class UpdateSessaoEvento(UpdateView):
    model = SessaoEvento
    #form_class = FormUpSessEv
    fields = ['evento', 'descr', 'regras', 'dataini', 'datafim', 'ativo']
    template_name = "eventos/form.html"
    success_url = reverse_lazy('eventos:listar-sessao-evento')
    
    widgets = {
        'dataini': forms.DateField(
            required=True,
            widget=forms.TextInput(attrs={'type': 'date'})
            ),
        'datafim': forms.DateInput(
            format=('%d/%m/%Y'),          # <== This line solves the issue
            attrs={'class': 'form-control',
                   'type': 'date'
            }),
    }

#---- Excluir ----#

class DeleteEvento(DeleteView):
    model = Evento
    fields = ['descr', 'ativo']
    template_name = "eventos/form_ex.html"
    success_url = reverse_lazy('eventos:listar-evento')

class DeletePublico(DeleteView):
    model = Publico
    fields = ['nick', 'email', 'ativo', 'publico_filho']
    template_name = "eventos/form_ex.html"
    success_url = reverse_lazy('eventos:listar-publico')

class DeleteSessaoEvento(DeleteView):
    model = SessaoEvento
    fields = ['descr', 'regras', 'dataini', 'datafim', 'evento']
    template_name = "eventos/form_ex.html"
    success_url = reverse_lazy('eventos:listar-sessao-evento')

#---- List Views ----#

class ListEvento(ListView):
    model = Evento
    template_name = "eventos/list/evento.html"

class ListSessaoEvento(ListView):
    model = SessaoEvento
    template_name = "eventos/list/sessao.html"

class ListPublico(ListView):
    model = Publico
    template_name = "eventos/list/publico.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
#        context['now'] = timezone.now()
        return context


#---- Importacao ----#

def ImportaEvento(request):
    if __name__ == '__main__' and __package__ is None:
        from os import sys, path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    path = os.getcwd()
    if 'cargas' in path:
        filepath = ''
    else:
        filepath = 'cargas/'
    
    wb = load_workbook(filename=filepath+"estrutura.xlsx")

    #Evento.objects.all().delete()

    InicEst = wb['Evento']
    
    for i, row in enumerate(InicEst):
        if i>0:
            SessaoEvento.objects.update_or_create(descr=row[0].value
                )
 
    InicEst = wb['Grupo']
    
    for i, row in enumerate(InicEst):
        if i>0:
            Grupo.objects.update_or_create(nome=row[0].value
                )
 
    InicEst = wb['Jogadores']

    for i, row in enumerate(InicEst):
        if i>0:
            orc = Grupo.objects.get(nome=row[4].value)
            Publico.objects.update_or_create(grupo=orc, 
                nick=row[3].value,
                )

    return render(request, 'eventos/index.html')

