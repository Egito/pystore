# Generated by Django 3.1.3 on 2021-08-15 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_auto_20210814_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publico',
            name='publico_filho',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='eventos.publico', verbose_name='Publico Filho'),
        ),
    ]
