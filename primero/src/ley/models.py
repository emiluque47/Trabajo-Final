from django.db import models
import datetime
# Create your models here.

class Formularios_Ley(models.Model):
	id 						= models.BigAutoField(primary_key=True, unique=True)
	nombre					= models.CharField(max_length=30, null=False, blank=False)
	apellido				= models.CharField(max_length=30, null=False, blank=False)
	correo					= models.CharField(max_length=30, null=False, blank=False)
	nacimiento				= models.DateField(verbose_name='nacimiento', default=datetime.date.today )
	comentario				= models.TextField(blank=True)
	
	def __str__(self):
		return self.apellido + ' ' + self.nombre

