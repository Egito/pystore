from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from model_utils.models import TimeStampedModel

class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)

class Parcel(TimeStampedModel):
    comment = models.TextField(blank=True)
    status = models.CharField(max_length=255)
    parcel = models.DecimalField(max_digits=4, decimal_places=0)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    datep = models.DateField(auto_now=False, auto_now_add=False)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("status",)
        verbose_name = "parcel"
        verbose_name_plural = "parcels"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('parcels:detail', kwargs={"id": self.id})

class N_Orcamento(models.Model):
    entrega = models.ForeignKey(Entrega, on_delete=models.CASCADE, null=True, blank=True)
    tipocusto = models.IntegerField(choices=N_TIPO_CUSTO, default=1)
    classecusto = models.ForeignKey(N_ClasseCusto, on_delete=models.CASCADE, null=True, blank=True)
    tipoPEP = models.ForeignKey(N_TipoPEP, on_delete=models.CASCADE, null=True, blank=True)
    fornecedor = models.CharField(max_length=100, null=False, blank=False, default='')
    cenario = models.IntegerField(choices=[(1,'Draft'), (2, 'Validado')], default=1)
    descricao = models.CharField(max_length=2000, null=True, blank=True)
    justificativa = models.CharField(max_length=2000, null=True, blank=True)
    ativo = models.BooleanField(default=True)

class N_Orcamento_TC(models.Model):
    orcamento = models.ForeignKey(N_Orcamento, on_delete=models.CASCADE, null=True, blank=True)
    sigitec = models.CharField(max_length=12, null=False, blank=False)
    status = models.CharField(max_length=30, choices=[('A Contratar', 'A Contratar'), ('Em Contratação', 'Em Contratação'), ('Contratado', 'Contratado')], default='Contratado')
    observacao = models.CharField(max_length=500, null=True, blank=True)

class N_Parcela(models.Model):
    orcamento = models.ForeignKey(N_Orcamento, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    parcela = models.IntegerField(validators=[MaxValueValidator(99)], null=True, blank=True)
    status_parcela = models.CharField(max_length=30, choices=[('A Pagar', 'A Pagar'), ('Paga', 'Paga')],default='A Pagar')
    obs_parcela = models.CharField(max_length=500, null=True, blank=True)
