
from django.urls import path
from grupos import views

app_name = 'grupos'

urlpatterns = [
    path('', views.index, name="grupo"),
    path('<acao_af>', views.index, name="grupo"),
    path('del/<item_id>/<acao_af>', views.remove, name="del"),
    path('carga/', views.carga, name="carga"),
]
