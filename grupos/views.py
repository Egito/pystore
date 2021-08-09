import os
import django

from openpyxl import load_workbook
from django.shortcuts import render, redirect
from django.contrib import messages
 
from .forms import GruposForm, JogadoresForm
from .models import Grupos, Jogadores
 
###############################################
 
def index(request, acao_af="gru"):
 
    if request.method == "POST":
        if acao_af == "gru":
            form = GruposForm(request.POST)
        elif acao_af == "jog":
            form = JogadoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/grupos',acao_af=acao_af)

    if acao_af == "gru":
        form = GruposForm()
        item_list = Grupos.objects.all()
    elif acao_af == "jog":
        form = JogadoresForm()
        item_list = Jogadores.objects.all()
#    else:
#        item_list = Orcamento.objects.all()
 
    page = {
             "forms" : form,
             "item" : item_list,
             "acao_af" : acao_af,
             "title" : "TODO LIST",
           }
    
    return render(request, 'grupos/index.html', page)

### function to remove item, it receive todo item id from url ##
def remove(request, item_id, acao_af):
    if acao_af == "gru":
        item = Grupos.objects.get(id=item_id)
    elif acao_af == "jog":
        item = Jogadores.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('/grupos',acao_af=acao_af)

def carga(request):
    if __name__ == '__main__' and __package__ is None:
        from os import sys, path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    path = os.getcwd()
    if 'cargas' in path:
        filepath = ''
    else:
        filepath = 'cargas/'
    
    wb = load_workbook(filename=filepath+"estrutura.xlsx")

    Grupos.objects.all().delete()

    InicEst = wb['Grupos']
    
    for i, row in enumerate(InicEst):
        if i>0:
            Grupos.objects.update_or_create(nome=row[0].value
                )
 
    InicEst = wb['Jogadores']

    for i, row in enumerate(InicEst):
        if i>0:
            orc = Grupos.objects.get(nome=row[4].value)
            Jogadores.objects.update_or_create(grupo=orc, 
                nick=row[3].value,
                )

    return redirect('/grupos')

