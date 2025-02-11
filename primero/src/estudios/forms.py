from django import forms
from django.forms import ModelForm
from estudios.models import Estudio

TIPOS_ESTUDIO = {
	'Biopsia':'Biopsia',
	'Análisis de Sangre':'Análisis de Sangre',
	'Resonancia Magnética': 'Resonancia Magnética',
	'Otro' : 'Otro',
}

class CargaEstudio(ModelForm):
	class Meta:
		model = Estudio
		fields = ('paciente','tipoEstudio','archivo', 'comentario')
		labels = {
			'paciente' : 'Seleccione un paciente',
			'tipoEstudio' : 'Seleccione el tipo de estudio',
			'archivo' : 'Seleccione un archivo',
			'comentario' : 'Comentario pertinente al estudio (opcional)'
		}
		widgets = {
			'paciente': forms.Select(attrs={'class':'form-control'}),
			'tipoEstudio':forms.Select(
				attrs={'class':'form-control'},
				choices=[
				('Biopsia','Biopsia'),
				('Análisis de Sangre','Análisis de Sangre'),
				('Resonancia Magnética', 'Resonancia Magnética'),
				('Otro' , 'Otro'),
				]),
			'comentario': forms.Textarea(attrs={'class':'form-control','rows':'3'})
		}