from django.db import models
from django.contrib.postgres.fields import ArrayField
from account.models import Account
from pacientes.models import Paciente
import datetime

# Create your models here.
class Solicitudes(models.Model):
	id 						= models.BigAutoField(primary_key=True, unique=True)
	medico					= models.ForeignKey(Account, blank=True, null= True, on_delete=models.CASCADE)
	paciente				= models.ForeignKey(Paciente, null=False, blank=False, on_delete=models.CASCADE) #esto es el id del paciente
	fecha_simulacion		= models.DateTimeField(verbose_name='Fecha de Solicitud', default=datetime.datetime.now())
	comentario				= models.CharField(max_length=300, null=False, blank=False)
	def __str__(self):
		return self.medico.username + ' ' + self.paciente.alias

class Respuesta(models.Model):
	id 						= models.BigAutoField(primary_key=True, unique=True)
	formulario				= models.ForeignKey(Solicitudes, blank=True, null= True, on_delete=models.CASCADE)
	comentario				= models.CharField(max_length=300, null=False, blank=False)
	archivo					= models.FileField(blank=False)
	def __str__(self):
		return self.comentario