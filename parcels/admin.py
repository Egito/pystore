from django.contrib import admin

from .models import Parcel

@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ["parcel", "value", "datep", "status", "comment", "created", "modified"]
