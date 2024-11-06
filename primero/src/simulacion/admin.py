from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Form_Sim
# Register your models here.

class AdminFormReq(UserAdmin):
	list_display =('medico','paciente','estudio1','comentario','fecha_estudio')
	search_fields =['medico']
	filter_horizontal =()
	list_filter=()
	fieldsets=()
	ordering = ['id']

admin.site.register(Form_Sim, AdminFormReq)