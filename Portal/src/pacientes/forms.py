from django import forms
from django.forms import ModelForm
from pacientes.models import Paciente

class CargaPaciente(ModelForm):
	class Meta:
		model = Paciente
		fields = ('alias','sexo','etnia','nacimiento','edad','peso','altura','comentario')
		labels = {
			'alias': 'Ingrese un Alias para el paciente',
			'sexo': 'Sexo del paciente',
			'etnia': 'Etnia del paciente',
			'nacimiento': 'Seleccione la fecha de nacimiento',
			'edad': 'Edad del paciente',
			'peso':'Peso (kg)',
			'altura': 'Altura (cm)',
			'comentario': 'Comentario pertinente al paciente (opcional)'
		}
		widgets = {
			'alias': forms.TextInput(attrs={'class':'form-control'}),
			'sexo': forms.TextInput(attrs={'class':'form-control'}),
			'etnia': forms.TextInput(attrs={'class':'form-control'}),
			'nacimiento': forms.DateInput(attrs={'class':'form-control','type':'date'}),
			'edad': forms.NumberInput(attrs={'class':'form-control'}),
			'peso': forms.NumberInput(attrs={'class':'form-control'}),
			'altura': forms.NumberInput(attrs={'class':'form-control'}),
			'comentario': forms.Textarea(attrs={'class':'form-control','rows':'3'})
		}