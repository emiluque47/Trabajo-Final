from django import forms
from estudios.models import Estudio

class CargaEstudio(forms.ModelForm):
	class Meta:
		model = Estudio
		fields = ('medico','paciente','aliaspaciente','tipoEstudio','imagen','archivo')