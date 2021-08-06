from django.contrib import admin

from .models import Parcela

@admin.register(Parcela)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ["parcela", "valor", "data", "status_parcela", "obs_parcela"]
