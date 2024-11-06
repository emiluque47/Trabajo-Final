from django import forms
from simulacion.models import Form_Sim

class ReqSimu (forms.ModelForm):
	class Meta:
		model = Form_Sim
		fields = ('medico','paciente','estudio1','comentario')