from django.contrib import admin

from .models import Radios

@admin.register(Radios)
class RadiosAdmin(admin.ModelAdmin):
    list_display = ["serial", "ativo"]
