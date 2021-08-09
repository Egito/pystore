from django.urls import path
from .views import myview

app_name = 'myapp'

urlpatterns = [
    path('', myview, name='myview')
]
