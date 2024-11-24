from django.shortcuts import render, redirect
from pacientes.models import Paciente
from estudios.models import Estudio
from simulacion.models import Solicitudes, Respuesta
from .forms import FormSolicitudes, FormRespuesta
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
def req_simulacion_view(request): #ya no lo uso
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_investigador:
		return redirect("login")
	context={}
	formulario = FormSolicitudes()
	user = request.user.username
	listapacientes = Paciente.objects.all().filter(medico__username=user)
	listaestudios = Estudio.objects.all()
	context['listapacientes']=listapacientes
	context['listaestudios']=listaestudios
	if request.method == 'POST':
		print("Es post")
		formulario = FormSolicitudes(request.POST)
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
			return redirect('listado_paciente')
	return render(request, 'simulacion/formulario.html', context)

#esto es el formulario de solicitud del medico
def solicitud_simulacion_view(request):
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_doctor:
		return redirect("login")
	
	context={}
	user = request.user.username
	useremail = request.user.email
	formulario= FormSolicitudes()
	listapacientes = Paciente.objects.all().filter(medico__username=user)
	listaestudios = Estudio.objects.all().filter(medico=useremail) #no usa __ porque el medico es parte del estudio, no un foreignkey
	context['listapacientes'] = listapacientes
	context['listaestudios'] = listaestudios
	context['solicitudes'] = formulario
	if request.method == 'POST':
		print("Es post")
		idverificar=request.POST['paciente']
		verificarestudios=listaestudios.all().filter(paciente__id=idverificar)
		verificarestudios.exists()
		print(verificarestudios.exists())
		formulario = FormSolicitudes(request.POST)
		if verificarestudios.exists():
			if formulario.is_valid():
				print("Es valid")
				carga = formulario.save(commit=False)
				carga.medico= request.user
				carga.save()
				return redirect('lista_simulacion')
		else:
			messages.success(request,("Por favor elija un usuario con estudios cargados"))
			return redirect ('solicitud_simulacion')
	return render (request, 'simulacion/solicitud_simulacion.html',context)

#esto muestra la lista de las solicitudes enviadas por el médico
#el boton resultado de simulaciones
def list_simulacion_view(request): 
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_doctor:
		return redirect("login")
	context={}
	print("list_simulacion_view")
	listaSimulaciones = Solicitudes.objects.all().filter(medico__username=request.user.username).order_by('-id')
	p = Paginator(listaSimulaciones,2)
	pagina = request.GET.get('page')
	simulaciones = p.get_page(pagina)
	context['simulaciones'] = simulaciones
	context['listaSimulaciones'] = listaSimulaciones
	return render(request, 'simulacion/listado.html', context)

#listado de solicitudes pantalla investigador
#el boton verde que dice Solicitudes
def listado_solicitudes_view(request):
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_investigador:
		return redirect("login")
	context={}
	print("listado_solicitudes_view")
	listaSimulaciones = Solicitudes.objects.all().order_by('-id')
	p = Paginator(listaSimulaciones,2)
	pagina = request.GET.get('page')
	simulaciones = p.get_page(pagina)
	context['simulaciones'] = simulaciones
	context['listaSimulaciones'] = listaSimulaciones
	return render(request, 'simulacion/listado_solicitudes.html', context)

#esta es la pantalla de datos de las solicitudes del medico
def datos_simulacion_medico_view(request,idSimulacion): 
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_doctor:
		return redirect("login")
	context={}
	listaSimulaciones = Solicitudes.objects.all().order_by('-id')
# 	context['listaSimulaciones'] = listaSimulaciones
	simu = Solicitudes.objects.get(id=idSimulacion)#obtengo la simulacion
	idpaciente = simu.paciente.id
	listaEstudios = Estudio.objects.all().filter(paciente_id=idpaciente) #obtengo los estudio
	paciente = Paciente.objects.all().filter(id=idpaciente)#obtengo el paciente
	listaRespuestas = Respuesta.objects.all().filter(formulario__paciente__id=idpaciente)
# 	rtasimulacion = Respuesta.objects.all().filter(idformulario=idSimulacion) #obtengo la respuesta
# 	print(rtasimulacion)
	context['listaRespuestas'] = listaRespuestas
	context['simulacion'] = simu
	context['listaEstudios'] = listaEstudios
	context['paciente'] = paciente
# 	context['respuesta'] = rtasimulacion
	return render(request, 'simulacion/datos_simulacion_medico.html', context)

#esta pantalla muestra al investigador todas las respuestas enviadas
#boton lista de respuestas
def list_respuestas_view(request):
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_investigador:
		return redirect("login")
	context={}
	print("list_respuestas_view")
	listarespuesta = Respuesta.objects.all()
	p = Paginator(listarespuesta,1)
	pagina = request.GET.get('page')
	respuestas = p.get_page(pagina)
	context['respuestas'] = respuestas
	return render(request, 'simulacion/lista_respuestas.html', context)

#esta es la pantalla de carga de respuesta
def datos_simulacion_view(request, idSimulacion):
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_investigador:
		return redirect("login")
	context={}
	form= FormRespuesta()
	#listaSimulaciones = Solicitudes.objects.all().order_by('-id')
	#context['listaSimulaciones'] = listaSimulaciones
	solic = Solicitudes.objects.get(pk=idSimulacion)#obtengo la simulacion
	idpaciente = solic.paciente.id
	#print(solic.paciente.id)
	listaEstudios = Estudio.objects.all().filter(paciente_id=idpaciente)
	paciente = Paciente.objects.get(id=idpaciente)#obtengo el paciente
	context['form']=form
	context['simulacion'] = solic
	context['listaEstudios'] = listaEstudios
	context['paciente'] = paciente
	if request.method == 'POST':
		#print("es un post")
		data = request.POST
		archivo2 = request.FILES.get('archivo')
		#print("data: ", data)
		forma = FormRespuesta(request.POST, request.FILES)
		if forma.is_valid():
			carga = forma.save(commit=False)
			carga.formulario = Solicitudes.objects.get(pk=idSimulacion)
			carga.save()
			#print(forma.formulario)
	#print(paciente[0]) #esto solo me da los valores del __str__(self), pero lo mismo tengo acceso a todo
	#print(simu[0].aliaspaciente) #YESSSSSSSSSSSSSS ESTO ME DA ACCESO AL DATO ALIASPACIENTE
	return render(request, 'simulacion/datos_simulacion.html', context)

#esto se encarga de borrar la solicitud
def borrar_solicitud_view(request, idSolicitud):
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_doctor:
		return redirect("home")
	solicitud = Solicitudes.objects.get(pk=idSolicitud)
	solicitud.delete()
	return redirect('lista_simulacion')

#esto se encarga de borrar respuestas
def borrar_respuesta_view(request, idRespuesta):
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_investigador:
		return redirect("home")
	respuesta = Respuesta.objects.get(pk=idRespuesta)
	respuesta.delete()
	return redirect('lista_respuestas')