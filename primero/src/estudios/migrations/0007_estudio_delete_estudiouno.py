# Generated by Django 4.2.11 on 2024-10-17 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudios', '0006_alter_estudiouno_aliaspaciente_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('medico', models.CharField(default='no', max_length=30)),
                ('paciente', models.CharField(max_length=30)),
                ('tipoEstudio', models.CharField(default='asd', max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='EstudioUno',
        ),
    ]
