# Generated by Django 4.2.11 on 2024-11-20 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0012_alter_paciente_medico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='altura',
            field=models.IntegerField(verbose_name='altura'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='edad',
            field=models.IntegerField(verbose_name='edad'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='peso',
            field=models.IntegerField(verbose_name='peso'),
        ),
    ]
