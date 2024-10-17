from django.contrib import admin
from .models import Estudio
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AdminEstudio(UserAdmin):
	list_display =('id', 'medico','paciente','tipoEstudio')
	search_fields =['medico']
	filter_horizontal =()
	list_filter=()
	fieldsets=()
	ordering = ['id']

admin.site.register(Estudio, AdminEstudio)