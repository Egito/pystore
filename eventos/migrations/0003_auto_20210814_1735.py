# Generated by Django 3.1.3 on 2021-08-14 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20210814_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessaoevento',
            name='datafim',
        ),
        migrations.RemoveField(
            model_name='sessaoevento',
            name='dataini',
        ),
    ]