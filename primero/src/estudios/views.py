from django.shortcuts import render
from .forms import CargaEstudio
from pacientes.models import Paciente
from account.models import Account

# Create your views here.

def carga_estudio_view(request):
	form = CargaEstudio()
	user = request.user.username
	context={}
	listapacientes = Paciente.objects.all().filter(medico=user)
	if request.method == 'POST':
		print("if pre valid")
		form = CargaEstudio(request.POST)
		if form.is_valid():
			form.save()
			print("yaaaay")
	context = {'form':form}
	context['listapacientes']=listapacientes
	return render(request, 'estudios/carga_estudio.html', context)

def listado_pacientes_estudio_view(request):
	user = request.user.username
	print(user)
	context = {}
	listapacientes = Paciente.objects.all().filter(medico=user)
	context['listapacientes']=listapacientes
	return render(request, 'estudios/carga_estudio.html',context)

def formulario_lista_estudios_view(request):
	user = request.user.username
	print(user)
	context = {}
	listapacientes = Paciente.objects.all().filter(medico=user)
	context['listapacientes']=listapacientes
	return render(request, 'estudios/formulario_lista_estudios.html',context)