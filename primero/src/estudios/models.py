from django.db import models

# Create your models here.
class EstudioUno(models.Model):
	id 						= models.BigAutoField(primary_key=True, unique=True)
	aliaspaciente			= models.CharField(max_length=30, null=False, blank=False)
	campo1					= models.CharField(max_length=3, null=False, blank=False, default="asd")
	campo2					= models.IntegerField(verbose_name='campo2', default="0")
	campo3					= models.IntegerField(verbose_name='campo3', default="0")
	
	def __str__(self):
		return self.aliaspaciente + self.campo1