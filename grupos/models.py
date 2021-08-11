from django.db import models
from django.utils import timezone
from model_utils.models import TimeStampedModel

class Grupo(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ("nome",)
        verbose_name = "grupo"

    def __str__(self):
        return self.nome

class Publico(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True, blank=True)
    nick = models.CharField(max_length=100, null=False, blank=False)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ("grupo", "nick",)
        verbose_name = "publico"
