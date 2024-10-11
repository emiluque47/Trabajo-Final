from django import forms
from pacientes.models import Paciente

class CargaPaciente(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = ('medico','alias','sexo','nacimiento','edad','peso','altura')