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
	return render (request,"equipo/equipo_single_1.html",{})

def team_single_view_2(request):
	return render (request,"equipo/equipo_single_2.html",{})

def team_single_view_3(request):
	return render (request,"equipo/equipo_single_3.html",{})

def team_single_view_4(request):
	return render (request,"equipo/equipo_single_4.html",{})

def team_single_view_5(request):
	return render (request,"equipo/equipo_single_5.html",{})

def team_single_view_6(request):
	return render (request,"equipo/equipo_single_6.html",{})	