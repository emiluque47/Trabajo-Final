# Generated by Django 4.2.11 on 2024-11-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0014_remove_paciente_raza_paciente_etnia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='comentario',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='etnia',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(max_length=10),
        ),
    ]
