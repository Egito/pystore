from django.contrib import admin

from .models import Evento, SessaoEvento, Publico

admin.site.register(Evento)
admin.site.register(SessaoEvento)
admin.site.register(Publico)