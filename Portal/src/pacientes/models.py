from django.db import models
import datetime
from account.models import Account
# Create your models here.

class Paciente(models.Model):
	id 						= models.BigAutoField(primary_key=True, unique=True)
	medico					= models.ForeignKey(Account, blank=True, null= True, on_delete=models.CASCADE)
	alias					= models.CharField(max_length=30, null=False, blank=False)
	sexo					= models.CharField(max_length=10, null=False, blank=False)
	etnia					= models.CharField(max_length=30, null=False, blank=False)
	nacimiento				= models.DateField(verbose_name='nacimiento', default=datetime.date.today )
	edad					= models.IntegerField(verbose_name='edad', null=False, blank=False)
	peso					= models.IntegerField(verbose_name='peso', null=False, blank=False)
	altura					= models.IntegerField(verbose_name='altura', null=False, blank=False)
	comentario				= models.TextField(blank=True)
	
	def __str__(self):
		return self.alias

