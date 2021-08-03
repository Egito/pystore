from django.urls import path

from .views import ParcelsDetailView, ParcelsListView

app_name = 'parcels'

urlpatterns = [
    path('', ParcelsListView.as_view(), name='list'),
    path('<int:id>/', ParcelsDetailView.as_view(), name='detail'),
]
