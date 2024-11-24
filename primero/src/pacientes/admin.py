from django.contrib import admin
from .models import Paciente
from django.contrib.auth.admin import UserAdmin
# Register your models here.

##class AdminPacientes(UserAdmin):
##	list_display =('id','alias','sexo','medico','raza')
##	search_fields =['medico']
##	filter_horizontal =()
##	list_filter=()
##	fieldsets=()
##	ordering = ['id']

#admin.site.register(Paciente)
@admin.register(Paciente)
class AdminPaciente(admin.ModelAdmin):
	list_display =('id','alias','sexo','medico','etnia')
	ordering = ('id',)
	search_fields =('medico','alias')