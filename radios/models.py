from django.db import models
from django.utils import timezone
from model_utils.models import TimeStampedModel

class Radios(TimeStampedModel):
    serial = models.CharField(max_length=30, null=False, blank=False)
    itemPPU = models.CharField(max_length=30, null=False, blank=False)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ("serial",)
        verbose_name = "radio"

    def __str__(self):
        return self.serial

class TipoOperacao(TimeStampedModel):
    tipo = models.CharField(max_length=30, null=False, blank=False)
    operacao = models.CharField(max_length=1, null=False, blank=False, default='!')
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ("operacao", "tipo",)
        verbose_name = "tipo operacao"

    def __str__(self):
        return self.tipo

class CapaMov(TimeStampedModel):
    descricao = models.CharField(max_length=30, null=False, blank=False)
    origem = models.CharField(max_length=100, null=False, blank=False, default='!')
    datamov = models.DateField()
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ("descricao", )
        verbose_name = "capa movimento"

    def __str__(self):
        return self.tipo

class Movimento(TimeStampedModel):
    capa = models.ForeignKey(CapaMov, on_delete=models.CASCADE, null=True, blank=True)
    radio = models.ForeignKey(Radios, on_delete=models.CASCADE, null=True, blank=True)
    tipo = models.ForeignKey(TipoOperacao, on_delete=models.CASCADE, null=True, blank=True)

    descricao = models.CharField(max_length=30, null=False, blank=False)
    dado = models.CharField(max_length=30, null=False, blank=False)

    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ("radio", "dado",)
        verbose_name = "movimento radio"
