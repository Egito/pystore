from django.db import models
from django.utils import timezone
from model_utils.models import TimeStampedModel

class Orcamento(models.Model):
    entrega = models.IntegerField(default=1)
    tipocusto = models.IntegerField(default=1)
    classecusto = models.IntegerField(default=1)
    tipoPEP = models.IntegerField(default=1)
    fornecedor = models.CharField(max_length=100, null=True, blank=True, default='')
    cenario = models.IntegerField(choices=[(1,'Draft'), (2, 'Validado')], default=1)
    descricao = models.CharField(max_length=2000, null=True, blank=True)
    justificativa = models.CharField(max_length=2000, null=True, blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ("fornecedor",)
        verbose_name = "orcamento"

class Contrato(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE, null=True, blank=True)
    sigitec = models.CharField(max_length=12, null=False, blank=False)
    status = models.CharField(max_length=30, choices=[('A Contratar', 'A Contratar'), ('Em Contratação', 'Em Contratação'), ('Contratado', 'Contratado')], default='Contratado')
    observacao = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ("orcamento",)
        verbose_name = "contrato"

class Parcela(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    parcela = models.IntegerField(null=True, blank=True)
    status_parcela = models.CharField(max_length=30, choices=[('A Pagar', 'A Pagar'), ('Paga', 'Paga')],default='A Pagar')
    obs_parcela = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ("status_parcela",)
        verbose_name = "parcela"
