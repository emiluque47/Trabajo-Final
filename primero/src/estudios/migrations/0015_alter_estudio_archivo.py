# Generated by Django 4.2.11 on 2024-11-22 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudios', '0014_remove_estudio_aliaspaciente_remove_estudio_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudio',
            name='archivo',
            field=models.FileField(upload_to=''),
        ),
    ]
