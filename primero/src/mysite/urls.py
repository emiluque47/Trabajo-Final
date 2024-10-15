"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
""" esto es para el resete de password"""
from django.contrib.auth import views as auth_views

"""mis views"""
from personal.views import(
    home_screen_view,
    team_main_view,
    team_single_view,
    team_single_view_2,
    team_single_view_3,
    team_single_view_4,
    team_single_view_5,
    )
from account.views import(
    registration_view,
    logout_view,
    login_view,
    account_view,
    )
from pacientes.views import(
    paciente_carga_view,
    listado_pacientes_view,
    datos_paciente_view,
    )
from contacto.views import(
    contacto_view,
    )
from estudios.views import(
    carga_estudio_view,
    listado_pacientes_estudio_view,
    formulario_lista_estudios_view,
    )

urlpatterns = [
    #generales
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
    path('contacto/', contacto_view, name="contacto"),
    # equipo
    path('team_main/', team_main_view, name="team_main"),
    path('team_single/', team_single_view, name="team_single"),
    path('team_single_2/', team_single_view_2, name="team_single_2"),
    path('team_single_3/', team_single_view_3, name="team_single_3"),
    path('team_single_4/', team_single_view_4, name="team_single_4"),
    path('team_single_5/', team_single_view_5, name="team_single_5"),
    # paciente
    path('paciente_carga/', paciente_carga_view, name="carga_paciente"),
    path('listado_pacientes/', listado_pacientes_view, name="listado_paciente"),
    path('datos_paciente/', datos_paciente_view, name="datos_paciente"),
    # estudios
    path('estudio_carga/', carga_estudio_view, name="carga_estudio"),
    path('lista_estudio/', formulario_lista_estudios_view, name="lista_estudio_1"),
    #----------------------------------------Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
    ##esto es lo que agrega el comentario de youtube
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name=
        'registration/password_reset_confirm.html'), name='password_reset_confirm'),
    #----------------------------------------fin de passwords y eso
]
