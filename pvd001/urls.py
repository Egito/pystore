from django.urls import path

from .views import pvd001_detalhe

app_name = 'pvd001'

urlpatterns = [
    path("", pvd001_detalhe, name="detalhe"),
]
