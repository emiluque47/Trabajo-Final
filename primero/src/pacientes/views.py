from django.shortcuts import render, redirect
from .forms import CargaPaciente
from pacientes.models import Paciente
from account.models import Account
from estudios.models import Estudio

# Create your views here.

def paciente_carga_view(request):
	form = CargaPaciente()
	context={}
	if request.method == 'POST':
		print("if pre valid")
		form = CargaPaciente(request.POST)
		if form.is_valid():
			form.save()
			context['exito'] ="Paciente Cargado!"
			print(context['exito'])
			return redirect('listado_paciente')
	context = {'form':form}
	return render(request, 'pacientes/carga_paciente.html', context)

def listado_pacientes_view(request):
	user = request.user.username
	context = {}
	#listapacientes = Paciente.objects.all()
	listapacientes = Paciente.objects.all().filter(medico=user)
	context['listapacientes']=listapacientes
	return render(request, 'pacientes/lista_paciente.html',context)

def datos_paciente_view(request, idPaciente):
	user = request.user.username
	context = {}
	print(idPaciente)
	paciente = Paciente.objects.all().filter(id=idPaciente) #consigo los datos del paciente
	listaestudios = Estudio.objects.all().filter(paciente__exact=idPaciente)
	#listaestudios = Estudio.objects.all()
	context['paciente']= paciente
	context['listaestudios']= listaestudios
	print(paciente)
	return render(request, 'pacientes/datos_paciente.html',context)