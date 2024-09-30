from django.db import models

# Create your models here.

class Paciente(models.Model):
	#edad					= models.IntegerField(verbose_name="edad", default=0)
	medico					= models.CharField(max_length=30, null=False, blank=False, default="no")
	alias					= models.CharField(max_length=30, null=False, blank=False)
	sexo					= models.CharField(max_length=3, null=False, blank=False, default="asd")
	def __str__(self):
		return self.alias + self.sexo + self.medico