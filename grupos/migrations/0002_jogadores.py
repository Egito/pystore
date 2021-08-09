# Generated by Django 3.1.3 on 2021-08-07 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=100)),
                ('ativo', models.BooleanField(default=True)),
                ('grupo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grupos.grupos')),
            ],
            options={
                'verbose_name': 'jogador',
                'ordering': ('nick',),
            },
        ),
    ]
