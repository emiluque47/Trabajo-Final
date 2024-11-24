from django.db import models
from pacientes.models import Paciente

# Create your models here.

class Estudio(models.Model):
	id 						= models.BigAutoField(primary_key=True, unique=True)
	medico					= models.CharField(max_length=30, null=False, blank=False, default="no") #el ide del medico (no foreign key)
	#paciente				= models.CharField(max_length=30, null=False, blank=False) #esto es el id del paciente
	paciente				= models.ForeignKey(Paciente, null=False, blank=False, on_delete=models.CASCADE) #esto es el paciente
	#aliaspaciente			= models.CharField(max_length=30, null=False, blank=False,default="no") #esto es el alias
	tipoEstudio				= models.CharField(max_length=30, null=False, blank=False, default="asd")
	#imagen					= models.ImageField(default='fallback.png', blank=True)
	archivo					= models.FileField(blank=False)
	comentario				= models.TextField(blank=True)
	
	def __str__(self):
		return self.medico + ' ' + self.paciente.alias  + ' ' + self.tipoEstudio

