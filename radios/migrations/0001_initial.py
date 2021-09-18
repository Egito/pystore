# Generated by Django 3.1.3 on 2021-09-02 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CapaMov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30)),
                ('origem', models.CharField(default='!', max_length=100)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'capa movimento',
                'ordering': ('descricao',),
            },
        ),
        migrations.CreateModel(
            name='Radios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=30)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'radio',
                'ordering': ('serial',),
            },
        ),
        migrations.CreateModel(
            name='TipoOperacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('operacao', models.CharField(default='!', max_length=1)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'tipo operacao',
                'ordering': ('operacao', 'tipo'),
            },
        ),
        migrations.CreateModel(
            name='Movimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30)),
                ('dado', models.CharField(max_length=30)),
                ('ativo', models.BooleanField(default=True)),
                ('capa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='radios.capamov')),
                ('radio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='radios.radios')),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='radios.tipooperacao')),
            ],
            options={
                'verbose_name': 'movimento radio',
                'ordering': ('radio', 'dado'),
            },
        ),
    ]