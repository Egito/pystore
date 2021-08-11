import os
import django

from openpyxl import load_workbook
from django.shortcuts import render, redirect
from django.contrib import messages
 
from .forms import GrupoForm, PublicoForm
from .models import Grupo, Publico
 
###############################################
 
def index(request, acao_af="gru"):
 
    if request.method == "POST":
        if acao_af == "gru":
            form = GrupoForm(request.POST)
        elif acao_af == "jog":
            form = PublicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/grupos',acao_af=acao_af)

    if acao_af == "gru":
        form = GrupoForm()
        item_list = Grupo.objects.all()
    elif acao_af == "jog":
        form = PublicoForm()
        item_list = Publico.objects.all()
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
        item = Grupo.objects.get(id=item_id)
    elif acao_af == "jog":
        item = Publico.objects.get(id=item_id)
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

    Grupo.objects.all().delete()

    InicEst = wb['Grupos']
    
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

    return redirect('/grupos')

