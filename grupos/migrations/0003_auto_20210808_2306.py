# Generated by Django 3.1.3 on 2021-08-09 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0002_jogadores'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jogadores',
            options={'ordering': ('grupo', 'nick'), 'verbose_name': 'jogador'},
        ),
    ]
