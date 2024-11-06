from django.shortcuts import render
from .forms import CargaEstudio
from pacientes.models import Paciente
from account.models import Account
from estudios.models import Estudio

# Create your views here.

def carga_estudio_view(request):
	user = request.user.username
	listapacientes = Paciente.objects.all().filter(medico=user)
	form = CargaEstudio()
	data = request.POST
	imagen2 = request.FILES.get('imagen')
	archivo2 = request.FILES.get('archivo')
	context={}
	if request.method == 'POST':
		#print('paciente: ', data['paciente']) #con esto cosigo el valor del input "paciente" del request
		print('data: ', data)
		print('imagen: ', imagen2)
		print('archivo: ', archivo2)
		print("if pre valid")
		form = CargaEstudio(request.POST, request.FILES)
		if form.is_valid():
			#print(form['idpaciente'])
			form.save()
			context['exito'] ="DIE!"
			print(context['exito'])
	context = {'form':form}
	context['listapacientes']=listapacientes
	return render(request, 'estudios/carga_estudio.html', context)

def listado_pacientes_estudio_view(request):
	user = request.user.username
	#print(user)
	context = {}
	listapacientes = Paciente.objects.all().filter(medico=user)
	context['listapacientes']=listapacientes
	return render(request, 'estudios/carga_estudio.html',context)

def formulario_lista_estudios_view(request):
	user = request.user.username
	context = {}
	listaestudios = Estudio.objects.all()
	listaestudios = Estudio.objects.all().filter(medico=user)
	context['listaestudios'] = listaestudios
	#if request.method == 'POST':
		#form = CargaEstudio(request.POST)
		#aliasmucho = form['aliaspaciente']
		#print(aliasmucho.value)
	return render(request, 'estudios/formulario_lista_estudios.html',context)