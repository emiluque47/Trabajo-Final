from django.shortcuts import render
from pacientes.models import Paciente
from estudios.models import Estudio
from simulacion.models import Form_Sim, Respuesta
from .forms import ReqSimu, FormRespuesta

# Create your views here.
def req_simulacion_view(request):
	context={}
	formulario = ReqSimu()
	user = request.user.username
	listapacientes = Paciente.objects.all().filter(medico=user)
	listaestudios = Estudio.objects.all()
	context['listapacientes']=listapacientes
	context['listaestudios']=listaestudios
	if request.method == 'POST':
		print("Es post")
		formulario = ReqSimu(request.POST)
		#print(formulario.errors) fields = ('medico','paciente', 'aliaspaciente','estudio1', 'idestudio1','comentario')
		# print("Medico: ",formulario['medico'].value())
		# print("Paciente: ",formulario['paciente'].value())
		# print("Aliaspaciente: ",formulario['aliaspaciente'].value())
		# print("campo estudio1 (el alias de estudio): ",formulario['estudio1'].value())
		# print("campo idestudio1(el id del estudio): ",formulario['idestudio1'].value())
		# print("Comentario: ",formulario['comentario'].value())
		#print(formulario['comentario'].value()) #no borro esta linea porque me sirve para acceder al valor
		if formulario.is_valid():
			print("Es valido")
			formulario.save()
	return render(request, 'simulacion/formulario.html', context)

def list_simulacion_view(request):
	context={}
	listaSimulaciones = Form_Sim.objects.all().order_by('-id')
	context['listaSimulaciones'] = listaSimulaciones
	return render(request, 'simulacion/listado.html', context)

def list_respuestas_view(request):
	context={}
	respuestas = Respuesta.objects.all()
	context['respuestas'] = respuestas
	return render(request, 'simulacion/lista_respuestas.html', context)

def datos_simulacion_view(request, idSimulacion):
	context={}
	listaSimulaciones = Form_Sim.objects.all().order_by('-id')
	context['listaSimulaciones'] = listaSimulaciones
	simu = Form_Sim.objects.all().filter(id=idSimulacion)#obtengo la simulacion
	idpaciente = simu[0].paciente 
	idestudio = simu[0].idestudio1
	estudio = Estudio.objects.all().filter(id=idestudio) #obtengo el estudio
	paciente = Paciente.objects.all().filter(id=idpaciente)#obtengo el paciente
	context['simulacion'] = simu
	context['estudio'] = estudio
	context['paciente'] = paciente

	if request.method == 'POST':
		print("es un post")
		data = request.POST
		archivo2 = request.FILES.get('archivo')
		print("data: ", data)
		forma = FormRespuesta(request.POST, request.FILES)
		if forma.is_valid():
			forma.save()
			print("saved")

	#print(paciente[0]) #esto solo me da los valores del __str__(self), pero lo mismo tengo acceso a todo
	#print(simu[0].aliaspaciente) #YESSSSSSSSSSSSSS ESTO ME DA ACCESO AL DATO ALIASPACIENTE
	return render(request, 'simulacion/datos_simulacion.html', context)
