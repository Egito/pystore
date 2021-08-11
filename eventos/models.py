from django.db import models
from django.utils import timezone
from model_utils.models import TimeStampedModel

class Evento(models.Model):
    descr = models.CharField(max_length=100, null=False, blank=False)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ("descr",)

    def __str__(self):
        return self.descr

class SessaoEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True, blank=True)
    descr = models.CharField(max_length=100, null=False, blank=False)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ("evento", "descr",)
        verbose_name = "sessao"
        verbose_name_plural = "sessões"
