from django.contrib import admin
from .models import Formularios_Ley
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(Formularios_Ley)
class AdminFormularios_Ley(admin.ModelAdmin):
	list_display =('id','nombre','apellido','correo')
	ordering = ('id',)
	search_fields =('correo','apellido')