from django.shortcuts import render
from openpyxl import load_workbook
from django.forms import ModelForm
import os

from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Evento, SessaoEvento, Publico
from django.urls import reverse_lazy


class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['descr', 'ativo']

class SessaoEventoForm(ModelForm):
    class Meta:
        model = SessaoEvento
        fields = ['descr', 'regras', 'ativo', 'evento']

class PublicoForm(ModelForm):
    class Meta:
        model = Publico
        fields = ['nick', 'email', 'ativo', 'publico_filho']

def remove(request, acao_af, item_id):
    if acao_af == "evento":
        item = Evento.objects.get(id=item_id)
        item.delete()
    elif acao_af == "sessao":
        item = EventoSessao.objects.get(id=item_id)
        item.delete()
    else:
        item = Publico.objects.get(id=item_id)
        item.delete()

    messages.info(request, "item removed !!")
    success_url = reverse_lazy('eventos:index')

def update(request, acao_af, item_id):
    if acao_af == "evento":
        item_list = Evento.objects.get(id=item_id)
        form = EventoForm(instance=item_list)
    elif acao_af == "sessao":
        item_list = EventoSessao.objects.get(id=item_id)
        form = SessaoEventoForm(instance=item_list)
    else:
        item_list = Publico.objects.get(id=item_id)
        form = PublicoForm(instance=item_list)

    page = {
             "item" : None,
             "form" : form,
             "acao_af" : acao_af,
           }
    
    return render(request, 'eventos/index.html', page)

def processar(request, item_id):
    
    acao_af = request.POST.get('acao_af','')
    if  acao_af == "evento":
        item = Evento.objects.get(id=item_id)
        item_list = Evento.objects.all()
        form = EventoForm(instance=item)
    elif acao_af == "sessao":
        item = EventoSessao.objects.get(id=item_id)
        item_list = EventoSessao.objects.all()
        form = SessaoEventoForm(instance=item)
    else:
        item = Publico.objects.get(id=item_id)
        item_list = Publico.objects.all()
        form = PublicoForm(instance=item)

    print(form)
    page = {
             "item" : item_list,
             "form" : form,
             "acao_af" : acao_af,
           }
    
    return render(request, 'eventos/index.html', page)

def index(request, acao_af="evento"):

    if acao_af == "evento":
        item_list = Evento.objects.all()
        form = EventoForm()
    elif acao_af == "sessao":
        item_list = SessaoEvento.objects.all()
        form = SessaoEventoForm()
    else:
        item_list = Publico.objects.all()
        form = PublicoForm()
 
    page = {
             "item" : item_list,
             "form" : form,
             "acao_af" : acao_af,
           }
    
    return render(request, 'eventos/index.html', page)

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

