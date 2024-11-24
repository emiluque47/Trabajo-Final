from django.shortcuts import render, redirect
from .forms import CargaPaciente
from pacientes.models import Paciente
from account.models import Account
from estudios.models import Estudio

from django.core.paginator import Paginator
# Create your views here.
#esto se encarga de la carga del paciente
def paciente_carga_view(request):
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_doctor:
		return redirect("home")
	cargado = False
	form = CargaPaciente()
	user = request.user.username
	if request.method == 'POST':
		form = CargaPaciente(request.POST)
		if form.is_valid():
			carga= form.save(commit=False)
			carga.medico = request.user
			carga.save()
			#print("Paciente Cargado!")
			return redirect('carga_estudio')
	context = {'form':form}
	return render(request, 'pacientes/carga_paciente.html', context)

#se encarga de la pantalla de lista de pacientes ,y paginado)
def listado_pacientes_view(request):
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_doctor:
		return redirect("home")
	user = request.user.username
	context = {}
	listapacientes = Paciente.objects.filter(medico__username = user).order_by('id')
	p = Paginator(Paciente.objects.filter(medico__username = user),5)
	pagina = request.GET.get('page')
	pacientes = p.get_page(pagina)
	context['pacientes']=pacientes
	return render(request, 'pacientes/lista_paciente.html',context)
	
#esto es la pantalla de datos de un paciente en particular
def datos_paciente_view(request, idPaciente):
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_doctor:
		return redirect("home")
	user = request.user.username
	context = {}
	paciente = Paciente.objects.all().filter(id=idPaciente) #consigo los datos del paciente
	listaestudios = Estudio.objects.all().filter(paciente__exact=idPaciente)
	#listaestudios = Estudio.objects.all()
	context['paciente']= paciente
	context['listaestudios']= listaestudios
	return render(request, 'pacientes/datos_paciente.html',context)

#esta es la pantalla de modificar datos de un paciente en particular
def modificar_datos_paciente_view(request, idPaciente):
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_doctor:
		return redirect("home")
	user = request.user.username
	context = {}
	paciente = Paciente.objects.get(pk=idPaciente)
	form = CargaPaciente(request.POST or None, instance=paciente)
	if form.is_valid():
		form.save()
		return redirect('listado_paciente')
	#paciente = Paciente.objects.all().filter(id=idPaciente) #consigo los datos del paciente
	context['paciente']= paciente
	context['form']=form
	#formulario = CargaPaciente(request.POST, instance=paciente)
	#if formulario.is_valid():
		#formulario.save()
		#return redirect ('pacientes/lista_paciente.html')
	return render(request, 'pacientes/modificar_datos_paciente.html',context)

#esta "pantalla" borra el paciente idpaciente y reririge a la lista
def borrar_paciente_view(request, idPaciente):
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_doctor:
		return redirect("home")
	paciente = Paciente.objects.get(pk=idPaciente)
	paciente.delete()
	return redirect('listado_paciente')