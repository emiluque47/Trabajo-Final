# Generated by Django 4.2.11 on 2024-10-16 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiouno',
            name='campo1',
        ),
        migrations.RemoveField(
            model_name='estudiouno',
            name='campo2',
        ),
        migrations.RemoveField(
            model_name='estudiouno',
            name='campo3',
        ),
        migrations.AddField(
            model_name='estudiouno',
            name='idmedico',
            field=models.IntegerField(default='0', verbose_name='medico'),
        ),
        migrations.AddField(
            model_name='estudiouno',
            name='idpaciente',
            field=models.IntegerField(default='0', verbose_name='paciente'),
        ),
        migrations.AddField(
            model_name='estudiouno',
            name='tipoEstudio',
            field=models.CharField(default='default', max_length=3),
        ),
    ]
