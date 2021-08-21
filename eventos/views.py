from django.shortcuts import render
from openpyxl import load_workbook
from django import forms
import os

from .models import Evento, SessaoEvento, Publico
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

#from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

#---- Create Views ----#

class CreateEvento(GroupRequiredMixin, CreateView):
    group_required = ['ADM', 'EVENTO']
    model = Evento
    fields = ['descr']
    template_name = "eventos/form.html"
    success_url = reverse_lazy('eventos:listar-evento')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Novo Evento'

        return context

class CreatePublico(GroupRequiredMixin, CreateView):
    group_required = ['EVENTO']
    model = Publico
    fields = ['nick', 'email', 'publico_filho']
    template_name = "eventos/form.html"
    success_url = reverse_lazy('eventos:listar-publico')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Novo Publico'

        return context

class CreateSessaoEvento(GroupRequiredMixin, CreateView):
    group_required = ['EVENTO']
    model = SessaoEvento
    fields = ['evento', 'descr', 'regras', 'dataini', 'datafim']
    template_name = "eventos/form.html"
    success_url = reverse_lazy('eventos:listar-sessao-evento')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Nova Sessão de Evento'

        return context

#---- Atualizar ----#

class UpdateEvento(GroupRequiredMixin, UpdateView):
    group_required = ['ADM']
    model = Evento
    fields = ['descr', 'ativo']
    template_name = "eventos/form.html"
    success_url = reverse_lazy('eventos:listar-evento')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Evento, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Atualizar Evento'

        return context

class UpdatePublico(GroupRequiredMixin, UpdateView):
    group_required = ['EVENTO']
    model = Publico
    fields = ['nick', 'email', 'publico_filho', 'ativo']
    template_name = "eventos/form.html"
    success_url = reverse_lazy('eventos:listar-publico')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Atualizar Publico'

        return context

class UpdateSessaoEvento(GroupRequiredMixin, UpdateView):
    group_required = ['EVENTO']
    model = SessaoEvento
    fields = ['evento', 'descr', 'regras', 'dataini', 'datafim', 'ativo']
    template_name = "eventos/form.html"
    success_url = reverse_lazy('eventos:listar-sessao-evento')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(SessaoEvento, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Atualizar Sessão de Evento'

        return context

#---- Excluir ----#

class DeleteEvento(GroupRequiredMixin, DeleteView):
    group_required = ['ADM', 'EVENTO']
    model = Evento
    fields = ['descr', 'ativo']
    template_name = "eventos/form_ex.html"
    success_url = reverse_lazy('eventos:listar-evento')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Evento, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Excluir Evento'

        return context

class DeletePublico(GroupRequiredMixin, DeleteView):
    group_required = ['EVENTO']
    model = Publico
    fields = ['nick', 'email', 'ativo', 'publico_filho']
    template_name = "eventos/form_ex.html"
    success_url = reverse_lazy('eventos:listar-publico')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Excluir Publico'

        return context

class DeleteSessaoEvento(GroupRequiredMixin, DeleteView):
    group_required = ['EVENTO']
    model = SessaoEvento
    fields = ['descr', 'regras', 'dataini', 'datafim', 'evento']
    template_name = "eventos/form_ex.html"
    success_url = reverse_lazy('eventos:listar-sessao-evento')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(SessaoEvento, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Excluir Sessão de Evento'

        return context

#---- List Views ----#

class ListEvento(ListView):
    model = Evento
    template_name = "eventos/list/evento.html"

    def get_queryset(self):
        self.object_list = Evento.objects.filter(usuario=self.request.user)
        return self.object_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Listagem de Eventos'

        return context

class ListSessaoEvento(ListView):
    model = SessaoEvento
    template_name = "eventos/list/sessao.html"

    def get_queryset(self):
        self.object_list = SessaoEvento.objects.filter(usuario=self.request.user)
        return self.object_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Listagem de Sessões de Eventos'

        return context

class ListPublico(ListView):
    model = Publico
    template_name = "eventos/list/publico.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
#        context['now'] = timezone.now()
        return context

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Listagem de Publicos'

        return context


#---- Importacao ----#

def ImportaEvento(GroupRequiredMixin, request):
    group_required = ['ADM']
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

