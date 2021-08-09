from django.contrib import admin

from .models import Grupos

@admin.register(Grupos)
class GruposAdmin(admin.ModelAdmin):
    list_display = ["nome"]
