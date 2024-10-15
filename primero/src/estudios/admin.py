from django.contrib import admin
from .models import EstudioUno
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AdminEstudioUno(UserAdmin):
	list_display =('id','aliaspaciente','campo1','campo2', 'campo3')
	search_fields =['aliaspaciente']
	filter_horizontal =()
	list_filter=()
	fieldsets=()
	ordering = ['id']

admin.site.register(EstudioUno, AdminEstudioUno)