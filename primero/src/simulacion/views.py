from django.shortcuts import render
from pacientes.models import Paciente
from estudios.models import Estudio
from .forms import ReqSimu

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
		if formulario.is_valid():
			print("Es valido")
			formulario.save()
	return render(request, 'simulacion/formulario.html', context)