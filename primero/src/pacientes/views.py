from django.shortcuts import render
from .forms import CargaPaciente
from pacientes.models import Paciente
from account.models import Account

# Create your views here.

def paciente_carga_view(request):
	form = CargaPaciente()
	context={}
	if request.method == 'POST':
		print("if pre valid")
		form = CargaPaciente(request.POST)
		if form.is_valid():
			form.save()
			print("yaaaay")
			context['success_message'] ="Paciente Cargado!"
	context = {'form':form}
	return render(request, 'pacientes/carga_paciente.html', context)

def listado_pacientes_view(request):
	user = request.user.username
	context = {}
	#listapacientes = Paciente.objects.all()
	listapacientes = Paciente.objects.all().filter(medico=user)
	context['listapacientes']=listapacientes
	return render(request, 'pacientes/lista_paciente.html',context)

def datos_paciente_view(request):
	user = request.user.username
	context = {}
	listapacientes = Paciente.objects.all().filter(medico=user)
	context['listapacientes']=listapacientes
	return render(request, 'pacientes/datos_paciente.html',context)