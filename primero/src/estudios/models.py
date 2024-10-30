from django.db import models

# Create your models here.

class Estudio(models.Model):
	id 						= models.BigAutoField(primary_key=True, unique=True)
	medico					= models.CharField(max_length=30, null=False, blank=False, default="no")
	paciente				= models.CharField(max_length=30, null=False, blank=False)
	tipoEstudio				= models.CharField(max_length=30, null=False, blank=False, default="asd")
	imagen					= models.ImageField(default='fallback.png', blank=True)
	
	def __str__(self):
		return self.medico	+ self.paciente + self.tipoEstudio

