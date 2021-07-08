from django.urls import path

from .views import ProductsDetailView, ProductsListView

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='list'),
    path('<slug:slug>/', ProductsDetailView.as_view(), name='detail'),
    path('category/<slug:slug>/', ProductsListView.as_view(), name='list_by_category'),
]
