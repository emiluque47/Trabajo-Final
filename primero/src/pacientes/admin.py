from django.contrib import admin
from .models import Paciente
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class AdminPacientes(Paciente):
	#list_display =('fecha_nac','edad','alias')
	#search_fields =('fecha_nac')
	filter_horizontal =()
	list_filter=()
	fieldsets=()

admin.site.register(Paciente)