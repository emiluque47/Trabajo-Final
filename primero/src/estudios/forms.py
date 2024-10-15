from django import forms
from estudios.models import EstudioUno

class CargaEstudio(forms.ModelForm):
	class Meta:
		model = EstudioUno
		fields = ('aliaspaciente','campo1','campo2','campo3')