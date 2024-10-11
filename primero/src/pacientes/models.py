from django.db import models
import datetime
# Create your models here.

class Paciente(models.Model):
	id 						= models.BigAutoField(primary_key=True, unique=True)
	medico					= models.CharField(max_length=30, null=False, blank=False, default="no")
	alias					= models.CharField(max_length=30, null=False, blank=False)
	sexo					= models.CharField(max_length=3, null=False, blank=False, default="asd")
	nacimiento				= models.DateField(verbose_name='nacimiento', default=datetime.date.today )
	edad					= models.IntegerField(verbose_name='edad', default="0")
	peso					= models.IntegerField(verbose_name='peso', default="0")
	altura					= models.IntegerField(verbose_name='altura', default="0")
	
	def __str__(self):
		return self.alias + self.sexo + self.medico