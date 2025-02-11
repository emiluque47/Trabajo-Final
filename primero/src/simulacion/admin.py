from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Solicitudes, Respuesta
# Register your models here.

class AdminFormReq(admin.ModelAdmin):
	list_display =('medico','paciente','comentario','fecha_simulacion')
	search_fields =['medico']
	filter_horizontal =()
	list_filter=()
	fieldsets=()
	ordering = ['id']

admin.site.register(Solicitudes, AdminFormReq)

class AdminRespuesta(admin.ModelAdmin):
	list_display =('formulario', 'comentario', 'archivo')
	filter_horizontal =()
	list_filter=()
	fieldsets=()
	ordering = ['id']

admin.site.register(Respuesta, AdminRespuesta)