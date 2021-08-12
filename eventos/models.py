from sys import maxsize
from django.db import models
from django.utils import timezone
#from model_utils.models import TimeStampedModel

class Evento(models.Model):
    descr = models.CharField(max_length=100, null=False, blank=False, verbose_name='Descrição')
    ativo = models.BooleanField(default=True)
    class Meta:
        ordering = ("descr",)

    def __str__(self):
        return "{} ({})".format(self.descr)

class SessaoEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT, null=True, blank=True)
    descr = models.CharField(max_length=100, null=False, blank=False, verbose_name='Descrição')
    regras = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Regras', default='Sem Regras')
    dataini = models.DateField(auto_now=True, verbose_name='Data Inicio')
    datafim = models.DateField(auto_now=True, verbose_name='Data Encerramento')
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ("evento", "descr",)
        verbose_name = "sessao"
        verbose_name_plural = "sessões"

    def __str__(self):
        return "{} ({})".format(self.descr, self.evento.descr)

class Grupo(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False, verbose_name='Nome do Grupo')
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ("nome",)
        verbose_name = "grupo"

    def __str__(self):
        return self.nome

class Publico(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT, null=True, blank=True)
    nick = models.CharField(max_length=20, null=False, blank=False, verbose_name='Apelido')
    nome = models.CharField(max_length=100, null=True, blank=True, default='')
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ("grupo", "nick",)
        verbose_name = "publico"

    def __str__(self):
        return "{} ({})".format(self.nick, self.grupo.nome)

