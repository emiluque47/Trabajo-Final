# Generated by Django 4.2.11 on 2024-10-17 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudios', '0003_remove_estudiouno_aliaspaciente_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiouno',
            name='tipoEstudio',
        ),
    ]
