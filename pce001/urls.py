from django.urls import path

from .views import AboutPageView, HomePageView

app_name = 'pce001'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
