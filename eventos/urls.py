from django.urls import path
from .views import IndexView

app_name = 'eventos'

urlpatterns = [
    path('', IndexView.as_view(), name="eventos"),
]
