from django.urls import path
from eventos import views
from .views import CreateEvento, CreateSessaoEvento, ImportaEvento

app_name = 'eventos'

urlpatterns = [
    path('', views.index, name="index"),
    path('importar-eventos', views.ImportaEvento, name="importar-eventos"),
    path('criar-eventos', CreateEvento.as_view(), name="criar-eventos"),
    path('criar-sessao-eventos', CreateSessaoEvento.as_view(), name="criar-sessao-eventos"),

]
