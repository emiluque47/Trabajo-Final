# Generated by Django 4.2.11 on 2024-11-08 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulacion', '0008_form_sim_aliaspaciente_alter_form_sim_fecha_estudio'),
    ]

    operations = [
        migrations.AddField(
            model_name='form_sim',
            name='idestudio1',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AlterField(
            model_name='form_sim',
            name='fecha_estudio',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 8, 7, 48, 43, 162451), verbose_name='date joined'),
        ),
    ]
