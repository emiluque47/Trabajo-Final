from django.shortcuts import render, redirect
from .forms import Formulario_Class
from ley.models import Formularios_Ley
from django.core.paginator import Paginator

# Create your views here.
#pagina de informacion
def ley_datos_view(request):
	return render (request,"ley/info.html",{})

#pagina de formulario de solicictud
def ley_datos_formulario_view(request):
	form = Formulario_Class()
	if request.method == 'POST':
		form = Formulario_Class(request.POST)
		if form.is_valid():
			carga= form.save(commit=False)
			carga.save()
			return redirect('ley_datos')
	context = {'form':form}
	return render (request,"ley/ley_form.html", context)

#se encarga de la pantalla de lista de formularios y paginado
def listado_formulario_view(request):
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_admin:
		return redirect("home")
	user = request.user.username
	context = {}
	listaformularios = Formularios_Ley.objects.order_by('id')
	#listapacientes = Paciente.objects.filter(medico__username = user).order_by('id')
	p = Paginator(Formularios_Ley.objects.order_by('id'),5)
	pagina = request.GET.get('page')
	listaforms = p.get_page(pagina)
	context['listaforms']=listaforms
	return render(request, 'ley/ley_lista.html',context)

#la pantalla de UN formulario en particular
def datos_formulario_view(request, idFormulario):
	if not request.user.is_authenticated:
		return redirect("login")
	if not request.user.is_admin:
		return redirect("home")
	user = request.user.username
	context = {}
	formulario = Formularios_Ley.objects.all().filter(id=idFormulario) #consigo los datos del formulario
	#listaestudios = Estudio.objects.all().filter(paciente__exact=idPaciente)
	print(formulario)
	context['formulario']= formulario
	#context['listaestudios']= listaestudios
	return render(request, 'ley/datos_form.html',context)