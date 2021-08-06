# Generated by Django 3.1.3 on 2021-08-06 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0005_auto_20210805_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigitec', models.CharField(max_length=12)),
                ('status', models.CharField(choices=[('A Contratar', 'A Contratar'), ('Em Contratação', 'Em Contratação'), ('Contratado', 'Contratado')], default='Contratado', max_length=30)),
                ('observacao', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'contrato',
                'ordering': ('orcamento',),
            },
        ),
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrega', models.IntegerField(default=1)),
                ('tipocusto', models.IntegerField(default=1)),
                ('classecusto', models.IntegerField(default=1)),
                ('tipoPEP', models.IntegerField(default=1)),
                ('fornecedor', models.CharField(default='', max_length=100)),
                ('cenario', models.IntegerField(choices=[(1, 'Draft'), (2, 'Validado')], default=1)),
                ('descricao', models.CharField(blank=True, max_length=2000, null=True)),
                ('justificativa', models.CharField(blank=True, max_length=2000, null=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'orcamento',
                'ordering': ('fornecedor',),
            },
        ),
        migrations.CreateModel(
            name='Parcela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('parcela', models.IntegerField(blank=True, null=True)),
                ('status_parcela', models.CharField(choices=[('A Pagar', 'A Pagar'), ('Paga', 'Paga')], default='A Pagar', max_length=30)),
                ('obs_parcela', models.CharField(blank=True, max_length=500, null=True)),
                ('orcamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parcels.orcamento')),
            ],
            options={
                'verbose_name': 'parcela',
                'ordering': ('status_parcela',),
            },
        ),
        migrations.DeleteModel(
            name='Parcel',
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
        migrations.AddField(
            model_name='contrato',
            name='orcamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parcels.orcamento'),
        ),
    ]
