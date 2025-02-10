from django.contrib import admin
from .models import Estudio
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(Estudio)
class AdminEstudio(admin.ModelAdmin):
	list_display =('id', 'paciente','tipoEstudio')
	ordering = ('id',)