from django.urls import path
from eventos import views
from .views import CreatePublico, CreateEvento, CreateSessaoEvento, ImportaEvento
from .views import UpdatePublico, UpdateEvento, UpdateSessaoEvento
from .views import DeletePublico, DeleteEvento, DeleteSessaoEvento
from .views import ListPublico, ListEvento, ListSessaoEvento

app_name = 'eventos'

urlpatterns = [

    path('', ListEvento.as_view(), name="listar-evento"),
    
    path('importar-eventos', views.ImportaEvento, name="importar-eventos"),

    path('criar-evento', CreateEvento.as_view(), name="criar-evento"),
    path('criar-sessao-evento', CreateSessaoEvento.as_view(), name="criar-sessao-evento"),
    path('criar-publico', CreatePublico.as_view(), name="criar-publico"),

    path('atualizar-evento/<int:pk>', UpdateEvento.as_view(), name="atualizar-evento"),
    path('atualizar-sessao-eventos/<int:pk>', UpdateSessaoEvento.as_view(), name="atualizar-sessao-evento"),
    path('atualizar-publico/<int:pk>', UpdatePublico.as_view(), name="atualizar-publico"),

    path('excluir-evento/<int:pk>', DeleteEvento.as_view(), name="excluir-evento"),
    path('excluir-sessao-eventos/<int:pk>', DeleteSessaoEvento.as_view(), name="excluir-sessao-evento"),
    path('excluir-publico/<int:pk>', DeletePublico.as_view(), name="excluir-publico"),

    path('listar-publico/', ListPublico.as_view(), name="listar-publico"),
    path('listar-evento/', ListEvento.as_view(), name="listar-evento"),
    path('listar-sessao-evento/', ListSessaoEvento.as_view(), name="listar-sessao-evento"),
]
