from django import forms
from django.forms import ModelForm
from ley.models import Formularios_Ley

class Formulario_Class(ModelForm):
	class Meta:
		model = Formularios_Ley
		fields = ('nombre','apellido','correo','nacimiento','comentario')
		labels = {
			'nombre': 'Ingrese su nombre',
			'apellido': 'Ingrese su apellido',
			'correo': 'Ingrese su correo electronico',
			'nacimiento': 'Ingrese su fecha de nacimiento',
			'comentario': 'Comentario'
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'correo': forms.TextInput(attrs={'class':'form-control'}),
			'nacimiento': forms.DateInput(attrs={'class':'form-control','type':'date'}),
			'comentario': forms.Textarea(attrs={'class':'form-control','rows':'3'})
		}