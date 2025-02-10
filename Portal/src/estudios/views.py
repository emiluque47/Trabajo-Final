from django.shortcuts import render, redirect
from .forms import CargaEstudio
from pacientes.models import Paciente
from account.models import Account
from estudios.models import Estudio
from django.contrib import messages

#Se encarga de borrar el estudio idEstudio
def borrar_estudio_view(request, idEstudio):
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_doctor:
		return redirect("home")
	estudio = Estudio.objects.get(pk=idEstudio)
	estudio.delete()
	return redirect('listado_paciente')

#Esto maneja la pantalla de carga de estudio
def carga_estudio_view(request):
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_doctor:
		return redirect("home")
	user = request.user.username
	listapacientes = Paciente.objects.all().filter(medico__username = user)
	form = CargaEstudio()
	data = request.POST
	imagen2 = request.FILES.get('imagen')
	archivo2 = request.FILES.get('archivo')
	context={}
	if request.method == 'POST':
		form = CargaEstudio(request.POST, request.FILES)
		if form.is_valid():
			carga = form.save(commit=False)
			carga.medico = request.user.email
			carga.save()
			return redirect('solicitud_simulacion')
		else:
			messages.success(request,("Por favor verifique los datos cargados"))
			return redirect ('carga_estudio')
	context = {'form':form}
	context['listapacientes']=listapacientes
	return render(request, 'estudios/carga_estudio.html', context)
