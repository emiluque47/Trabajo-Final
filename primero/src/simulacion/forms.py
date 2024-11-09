from django import forms
from simulacion.models import Form_Sim, Respuesta

class ReqSimu (forms.ModelForm):
	class Meta:
		model = Form_Sim
		fields = ('medico','paciente', 'aliaspaciente','estudio1', 'idestudio1','comentario')

class FormRespuesta (forms.ModelForm):
	class Meta:
		model = Respuesta
		fields = ('idformulario', 'comentario', 'archivo')