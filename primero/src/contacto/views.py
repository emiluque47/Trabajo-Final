from django.shortcuts import render

# Create your views here.
def contacto_view(request):
	return render (request,"contacto.html",{})