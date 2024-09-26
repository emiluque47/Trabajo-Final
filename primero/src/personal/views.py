from django.shortcuts import render
from account.models import Account
# Create your views here.

def home_screen_view(request):
	context = {}
	accounts= Account.objects.all()
	context['accounts'] = accounts
	return render (request, "personal/home.html", context)

def team_main_view(request):
	return render (request,"equipo/equipo_main.html",{})

def team_single_view(request):
	return render (request,"equipo/equipo_single.html",{})