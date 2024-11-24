from django.db import models
from django.contrib.postgres.fields import ArrayField
from account.models import Account
from pacientes.models import Paciente
import datetime

# Create your models here.
class Solicitudes(models.Model):
	id 						= models.BigAutoField(primary_key=True, unique=True)
	#medico					= models.CharField(max_length=30, null=False, blank=False)
	medico					= models.ForeignKey(Account, blank=True, null= True, on_delete=models.CASCADE)
	paciente				= models.ForeignKey(Paciente, null=False, blank=False, on_delete=models.CASCADE) #esto es el id del paciente
	fecha_simulacion		= models.DateTimeField(verbose_name='Fecha de Solicitud', default=datetime.datetime.now()) #no debería decir fecha_estudio, sino simulacion
	#aliaspaciente			= models.CharField(max_length=30, null=False, blank=False, default="testing") #esto es el alias del paciente
	#estudio1				= models.CharField(max_length=30, null=False, blank=False) #esto está guardando el alias de estudio,
	#idestudio1				= models.CharField(max_length=30, null=False, blank=False, default="30") #esto es el id del estudio
	comentario				= models.CharField(max_length=30, null=False, blank=False)
	#
	#estudios				= ArrayField(
	#	ArrayField( models.IntegerField(verbose_name='estudio', blank=True))
	#	)
	def __str__(self):
		return self.medico.username + ' ' + self.paciente.alias

class Respuesta(models.Model):
	id 						= models.BigAutoField(primary_key=True, unique=True)
	formulario				= models.ForeignKey(Solicitudes, blank=True, null= True, on_delete=models.CASCADE)
	comentario				= models.CharField(max_length=30, null=False, blank=False)
	archivo					= models.FileField(blank=False)
	def __str__(self):
		return self.comentario