import os
import django

from openpyxl import load_workbook
from django.shortcuts import render, redirect
from django.contrib import messages
 
from .forms import RadioForm, MovimentoForm
from .models import Radios, Movimento
 
###############################################
 
def index(request, acao_af="radio"):
 
    if request.method == "POST":
        if acao_af == "radio":
            form = RadioForm(request.POST)
        elif acao_af == "movimento":
            form = MovimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/radios',acao_af=acao_af)

    if acao_af == "radio":
        form = RadioForm()
        item_list = Radios.objects.all()
    elif acao_af == "movimento":
        form = MovimentoForm()
        item_list = Movimento.objects.all()
#    else:
#        item_list = Orcamento.objects.all()
 
    page = {
             "forms" : form,
             "item" : item_list,
             "acao_af" : acao_af,
             "title" : "Controle de Radios",
           }
    
    return render(request, 'radios/index.html', page)

### function to remove item, it receive todo item id from url ##
def remove(request, item_id, acao_af):
    if acao_af == "radio":
        item = Radios.objects.get(id=item_id)
    elif acao_af == "movimento":
        item = Movimento.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('/radios',acao_af=acao_af)

def carga(request):
    # Open a file
    path = "previas/"
    dirs = os.listdir( path )

    #if arq=='':
    #    render(request, 'radios/seleciona.html', dirs)
    
    arq = 'previas/Arq.xlsx'

    wb = load_workbook(arq)

    #Radios.objects.all().delete()

    # carga de seriais
    InicEst = wb['PREVIA MOTOROLA TRK']
    
    for i, row in enumerate(InicEst):
        if i>14:
            Radios.objects.update_or_create(serial=row[2].value,
                itemPPU=row[11].value
                )
 
    # carga de seriais
    InicEst = wb['PREVIA MOTOROLA TRK']

    for i, row in enumerate(InicEst):
        if i==8:
            CapaMov.objects.update_or_create(descricao='Coleta de Previa',
                origem='Previa Motorola', 
                datamov=row[2].value
                )
            capam = CapaMov.objects.filter(descricao='Coleta de Previa',
                datamov=row[2].value
                )

        if i>14:
            # carrega movimento de inscricao inicial
            radio = Radios.objects.get(serial=row[2].value)

            # movimento = NF Motorola

            TipoOperacao.objects.update_or_create(tipo='NF Motorola',
                operacao='!'
                )
 
            opera = TipoOperacao.objects.get(tipo='NF Motorola')

            Movimento.objects.update_or_create(capa=capam,
                radio=radio, 
                tipo=tipo, 
                dado=row[4].value,
                descricao='Nota Fiscal - Motorola'
                )

            # movimento = Data da NF Motorola

            TipoOperacao.objects.update_or_create(tipo='Data NF Motorola',
                operacao='!'
                )
 
            opera = TipoOperacao.objects.get(tipo='Data NF Motorola')

            Movimento.objects.update_or_create(capa=capam,
                radio=radio, 
                tipo=tipo, 
                dado=row[5].value,
                descricao='Nota Fiscal - Motorola'
                )

            # movimento = Cobrança do Periodo

            TipoOperacao.objects.update_or_create(tipo='Cobrança do Periodo',
                operacao='!'
                )
 
            opera = TipoOperacao.objects.get(tipo='Cobrança do Periodo')

            Movimento.objects.update_or_create(capa=capam,
                radio=radio, 
                tipo=tipo, 
                dado=row[15].value,
                descricao='Quantidade'
                )

            # movimento = 

            TipoOperacao.objects.update_or_create(tipo='Municipio do Periodo',
                operacao='!'
                )
 
            opera = TipoOperacao.objects.get(tipo='Municipio do Periodo')

            Movimento.objects.update_or_create(capa=capam,
                radio=radio, 
                tipo=tipo, 
                dado=row[6].value,
                descricao='Municipio Informado'
                )

    return redirect('/radios')

