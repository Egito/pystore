import os
import django

from openpyxl import load_workbook
from django.shortcuts import render, redirect
from django.contrib import messages
 
from .forms import ParcelaForm
from .models import Parcela, Contrato, Orcamento
 
###############################################
 
def index(request, acao_af="parc"):
 
    if request.method == "POST":
        form = ParcelaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/parcelas')

    form = ParcelaForm()

    if acao_af == "parc":
        item_list = Parcela.objects.all()
    elif acao_af == "cont":
        item_list = Contrato.objects.all()
    else:
        item_list = Orcamento.objects.all()
 
    page = {
             "forms" : form,
             "item" : item_list,
             "acao_af" : acao_af,
             "title" : "TODO LIST",
           }
    
    return render(request, 'parcels/index.html', page)

### function to remove item, it receive todo item id from url ##
def remove(request, item_id):
    item = Parcela.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('/parcelas')

def carga(request):
    if __name__ == '__main__' and __package__ is None:
        from os import sys, path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    path = os.getcwd()
    if 'cargas' in path:
        filepath = ''
    else:
        filepath = 'cargas/'
    
    wb = load_workbook(filename=filepath+"map-e.xlsx")

    Parcela.objects.all().delete()
    Contrato.objects.all().delete()
    Orcamento.objects.all().delete()

    InicEst = wb['Entregas_N_Orcamento']
    
    for i, row in enumerate(InicEst):
        if i>0:
            Orcamento.objects.update_or_create(id=row[0].value, 
                tipocusto=row[1].value, 
                fornecedor=row[2].value,
                cenario=row[3].value,
                descricao=row[4].value,
                justificativa=row[5].value,
                ativo=row[6].value,
                classecusto=row[7].value,
                entrega=row[8].value,
                tipoPEP=row[9].value
                )
 
    InicEst = wb['Entregas_N_Orcamento_TC']

    for i, row in enumerate(InicEst):
        if i>0:
            orc = Orcamento.objects.get(id=row[4].value)
            Contrato.objects.update_or_create(orcamento=orc, 
                sigitec=row[1].value,
                status=row[2].value,
                observacao=row[3].value
                )

    InicEst = wb['Entregas_N_Parcela']

    for i, row in enumerate(InicEst):
        if i>0:
            orc = Orcamento.objects.get(id=row[6].value)
            Parcela.objects.update_or_create(orcamento=orc, 
                data=row[1].value,
                valor=row[2].value,
                parcela=row[3].value,
                status_parcela=row[4].value,
                obs_parcela=row[5].value
                )

    return redirect('/parcelas')

