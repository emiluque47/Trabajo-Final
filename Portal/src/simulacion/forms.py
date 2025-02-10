from django import forms
from simulacion.models import Solicitudes, Respuesta

class FormSolicitudes (forms.ModelForm):
	class Meta:
		model = Solicitudes
		fields = ('medico','paciente', 'comentario')
		labels = {
			'comentario': 'Comentario pertinente al paciente (opcional)'
		}
		widgets = {
			'comentario': forms.Textarea(attrs={'class':'form-control','rows':'3'})
		}

class FormRespuesta (forms.ModelForm):
	class Meta:
		model = Respuesta
		fields = ('formulario', 'comentario', 'archivo')
		labels = {
			'comentario': 'Comentario pertinente a la simluación (opcional)',
			'archivo' :'Cargar Archivo'
		}
		widgets = {
			'comentario': forms.Textarea(attrs={'class':'form-control','rows':'3'})
		}