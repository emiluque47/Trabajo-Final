from django.db import models
from pacientes.models import Paciente

# Create your models here.

class Estudio(models.Model):
	id 						= models.BigAutoField(primary_key=True, unique=True)
	medico					= models.CharField(max_length=30, null=False, blank=False, default="no")
	paciente				= models.ForeignKey(Paciente, null=False, blank=False, on_delete=models.CASCADE)
	tipoEstudio				= models.CharField(max_length=30, null=False, blank=False, default="asd")
	archivo					= models.FileField(blank=False)
	comentario				= models.TextField(blank=True)
	
	def __str__(self):
		return self.medico + ' ' + self.paciente.alias  + ' ' + self.tipoEstudio

