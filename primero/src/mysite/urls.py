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
""" esto es para el reset de password"""
from django.contrib.auth import views as auth_views
""" esto es para las imagenes """
from django.conf.urls.static import static
from django.conf import settings

"""mis views"""
from ley.views import(
    ley_datos_view,
    ley_datos_formulario_view,
    listado_formulario_view,
    datos_formulario_view,
    )
from personal.views import(
    home_screen_view,
    team_main_view,
    team_single_view,
    team_single_view_2,
    team_single_view_3,
    team_single_view_4,
    team_single_view_5,
    team_single_view_6,
    )
from account.views import(
    registration_view,
    logout_view,
    login_view,
    account_view,
    actualizar_datos_cuenta_view,
    )
from pacientes.views import(
    paciente_carga_view,
    listado_pacientes_view,
    datos_paciente_view,
    modificar_datos_paciente_view,
    borrar_paciente_view,
    )
from contacto.views import(
    contacto_view,
    )
from estudios.views import(
    carga_estudio_view,
    #listado_pacientes_estudio_view,
    #formulario_lista_estudios_view,
    borrar_estudio_view,
    )
from simulacion.views import(
    req_simulacion_view,
    list_simulacion_view,
    datos_simulacion_view,
    list_respuestas_view,
    datos_simulacion_medico_view,
    listado_solicitudes_view,
    solicitud_simulacion_view,
    borrar_solicitud_view,
    borrar_respuesta_view,
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
    path('datos_cuenta/', actualizar_datos_cuenta_view, name="datos_cuenta"),
    path('ley_datos/', ley_datos_view, name="ley_datos"),
    path('ley_datos/formulario', ley_datos_formulario_view, name="ley_form"),
    path('ley_datos/lista_forms', listado_formulario_view, name="ley_listado"),
    path('ley_datos/datos_form/<str:idFormulario>/', datos_formulario_view, name="datos_formulario"),
    # equipo
    path('team_main/', team_main_view, name="team_main"),
    path('team_single/', team_single_view, name="team_single"),
    path('team_single_2/', team_single_view_2, name="team_single_2"),
    path('team_single_3/', team_single_view_3, name="team_single_3"),
    path('team_single_4/', team_single_view_4, name="team_single_4"),
    path('team_single_5/', team_single_view_5, name="team_single_5"),
    path('team_single_6/', team_single_view_6, name="team_single_6"),
    # paciente
    path('paciente_carga/', paciente_carga_view, name="carga_paciente"),
    path('listado_pacientes/', listado_pacientes_view, name="listado_paciente"),
    path('datos_paciente/<str:idPaciente>/', datos_paciente_view, name="datos_paciente"),
    path('modificar_datos_paciente/<str:idPaciente>/', modificar_datos_paciente_view, name="modificar_datos_paciente"),
    path('borrar_paciente/<str:idPaciente>/', borrar_paciente_view, name="borrar_paciente"),
    # estudios
    path('estudio_carga/', carga_estudio_view, name="carga_estudio"),
    path('borrar_estudio/<str:idEstudio>/', borrar_estudio_view, name="borrar_estudio"),
    # simulacion
    path('simulacion/', req_simulacion_view, name="formulario_simulacion"),
    path('listado_simulacion/', list_simulacion_view, name="lista_simulacion"),
    path('datos_simulacion/<str:idSimulacion>/', datos_simulacion_view, name="datos_simulacion"),
    path('lista_respuestas/', list_respuestas_view, name="lista_respuestas"),
    path('datos_simulacion_medico/<str:idSimulacion>/', datos_simulacion_medico_view, name="datos_simulacion_medico"),
    path('listado_solicitudes/', listado_solicitudes_view, name="lista_solicitudes"),
    path('solicitud_simulacion/', solicitud_simulacion_view, name="solicitud_simulacion"),
    path('borrar_solicitud/<str:idSolicitud>/', borrar_solicitud_view, name="borrar_solicitud"),
    path('borrar_respuesta/<str:idRespuesta>/', borrar_respuesta_view, name="borrar_respuesta"),
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

""" tambien para imagenes """
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)