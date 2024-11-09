from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime

# Create your models here.
class Form_Sim(models.Model):
	id 						= models.BigAutoField(primary_key=True, unique=True)
	medico					= models.CharField(max_length=30, null=False, blank=False)
	fecha_estudio			= models.DateTimeField(verbose_name='date joined', default=datetime.datetime.now()) #no debería decir fecha_estudio, sino simulacion
	paciente				= models.CharField(max_length=30, null=False, blank=False) #esto es el id del paciente
	aliaspaciente			= models.CharField(max_length=30, null=False, blank=False, default="testing") #esto es el alias del paciente
	estudio1				= models.CharField(max_length=30, null=False, blank=False) #esto está guardando el alias de estudio, no el id
	idestudio1				= models.CharField(max_length=30, null=False, blank=False, default="30") #esto es el id del estudio
	comentario				= models.CharField(max_length=30, null=False, blank=False)
	#
	#estudios				= ArrayField(
	#	ArrayField( models.IntegerField(verbose_name='estudio', blank=True))
	#	)
	def __str__(self):
		return self.medico + self.paciente + self.estudio1 + self.comentario

class Respuesta(models.Model):
	id 						= models.BigAutoField(primary_key=True, unique=True)
	idformulario			= models.CharField(max_length=30, null=False, blank=False)
	comentario				= models.CharField(max_length=30, null=False, blank=False)
	archivo					= models.FileField(default='fallback.pdf', blank=True)
	def __str__(self):
		return self.idformulario + self.comentario