from django import forms
from pacientes.models import Paciente

class CargaPaciente(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = ('medico','alias','sexo','raza','nacimiento','edad','peso','altura')