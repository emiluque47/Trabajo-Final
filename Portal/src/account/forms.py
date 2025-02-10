from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import authenticate

from account.models import Account, DatosCuenta

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text='Requerido. Ingresar una dir valida')

	class Meta:
		model = Account
		fields = ("email", "username", "password1", "password2")

class AccountAuthenticationForm (forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	class Meta:
		model = Account
		fields = ('email','password')
	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid Login")

class AccountUpdateForm(forms.ModelForm):
	class Meta:
		model=Account
		fields=('email','username')
	def clean_email(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			try:
				account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
			except Account.DoesNotExist:
				return email
			raise forms.ValidationError('Email "%s" is already in use' % account)
	def clean_username(self):
		if self.is_valid():
			username = self.cleaned_data['username']
			try:
				account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
			except Account.DoesNotExist:
				return username
			raise forms.ValidationError('Username "%s" is already in use' % account.username)

class FormDatosCuenta (forms.ModelForm):
	class Meta:
		model=DatosCuenta
		fields=('nombre', 'apellido', 'especialidad', 'institucion', 'matricula')
		labels={
			'nombre':'Nombre',
			'apellido' : 'Apellido',
			'especialidad' : 'Especialidad',
			'institucion' : 'Institución',
			'matricula' : 'Matrícula',
		}
		widgets={
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'especialidad': forms.TextInput(attrs={'class':'form-control'}),
			'institucion': forms.TextInput(attrs={'class':'form-control'}),
			'matricula': forms.TextInput(attrs={'class':'form-control'}),
		}