from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime

# Create your models here.
class Form_Sim(models.Model):
	id 						= models.BigAutoField(primary_key=True, unique=True)
	medico					= models.CharField(max_length=30, null=False, blank=False)
	fecha_estudio			= models.DateTimeField(verbose_name='date joined', default=datetime.datetime.now())
	paciente				= models.CharField(max_length=30, null=False, blank=False)
	estudio1				= models.CharField(max_length=30, null=False, blank=False)
	comentario				= models.CharField(max_length=30, null=False, blank=False)
	#
	#estudios				= ArrayField(
	#	ArrayField( models.IntegerField(verbose_name='estudio', blank=True))
	#	)
	def __str__(self):
		return self.medico + self.paciente + self.estudio1 + self.comentario