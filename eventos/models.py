from sys import maxsize
from django import forms
from django.db import models
from django.conf import settings
from django.utils import timezone
#from model_utils.models import TimeStampedModel

class Evento(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    descr = models.CharField(max_length=100, unique=True, verbose_name='Descrição')
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ("descr",)

    def __str__(self):
        return "{}".format(self.descr)

class SessaoEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    descr = models.CharField(max_length=100, unique=True, verbose_name='Descrição da Sessão')
    regras = models.TextField(max_length=4000, null=False, verbose_name='Regras', default='Sem Regras')
    dataini = models.DateField(null=True, verbose_name='Data Inicio')
    datafim = models.DateField(null=True, verbose_name='Data Encerramento')
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ("descr",)
        verbose_name = "sessao"
        verbose_name_plural = "sessões"

    def __str__(self):
        return "{} ({})".format(self.descr, self.evento.descr)

class Publico(models.Model):
    nick = models.CharField(max_length=10, null=False, blank=False, verbose_name='Publico')
    email = models.CharField(max_length=100, null=False, blank=False, verbose_name='E-Mail')
    ativo = models.BooleanField(default=True)

    publico_filho = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True, related_name="children", verbose_name='Publico Filho')

    class Meta:
        ordering = ("nick",)
        verbose_name = "publico"

    def __str__(self):
        return "{} ({})".format(self.nick, self.email)
