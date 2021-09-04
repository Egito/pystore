
from django.urls import path
from radios import views

app_name = 'radios'

urlpatterns = [
    path('', views.index, name="radio"),
    path('<acao_af>', views.index, name="radio"),
    path('del/<item_id>/<acao_af>', views.remove, name="del"),
    path('carga/', views.carga, name="carga"),
]
