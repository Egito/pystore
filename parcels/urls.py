
from django.urls import path
from parcels import views

app_name = 'parcels'

urlpatterns = [
    path('', views.index, name="todo"),
    path('<acao_af>', views.index, name="todo"),
    ####################give id no. item_id name or item_id=i.id ############
    path('del/<item_id>', views.remove, name="del"),
    path('carga/', views.carga, name="carga"),
]
