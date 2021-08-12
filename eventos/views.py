from django.shortcuts import render
from openpyxl import load_workbook
import os

from django.views.generic import CreateView
from .models import Evento, SessaoEvento, Grupo, Publico
from django.urls import reverse_lazy

def index(request):
#    template_name = "eventos/form.html"
    return render(request, 'eventos/index.html')

class CreateEvento(CreateView):
    model = Evento
    fields = ['descr']
    template_name = "eventos/form.html"
    success_url = reverse_lazy('/')

class CreateSessaoEvento(CreateView):
    model = SessaoEvento
    fields = ['descr', 'regras', 'evento']
    template_name = "eventos/form.html"
    success_url = reverse_lazy('/')

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

