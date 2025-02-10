from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
	def create_user(self,email,username,password=None):
		if not email:
			raise ValueError("Usuarios deben tener email")
		if not username:
			raise ValueError("Usuarios deben tener nombre de usuario")

		user = self.model(
				email=self.normalize_email(email),
				username=username,
			)
		user.set_password(password)
		user.save(using=self._db)
		return user
	def create_superuser(self,email,username,password):
		user = self.create_user(
				email=self.normalize_email(email),
				password=password,
				username=username,
			)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):
	email					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username				= models.CharField(max_length=30, unique=True)
	nombre					= models.CharField(default='Nombre', max_length=30, blank=True)
	apellido				= models.CharField(default='Apellido', max_length=30, blank=True)
	especialidad			= models.CharField(default='Espcecialidad', max_length=30, blank=True)
	institucion				= models.CharField(default='Institucion', max_length=30, blank=True)
	matricula				= models.CharField(default='Matricula', max_length=30, blank=True)
	is_doctor				= models.BooleanField(default=False)
	is_investigador			= models.BooleanField(default=True)

	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return self.username + ", " + self.email
	def has_perm(self, perm, obj=None):
		return self.is_admin
	def has_module_perms(self, app_label):
		return True
	def return_username(self):
		return self.username

class DatosCuenta(models.Model):
	nombre					= models.CharField(default='Nombre', max_length=30)
	apellido				= models.CharField(default='Apellido', max_length=30)
	especialidad			= models.CharField(default='Especialidad', max_length=30, blank=True)
	institucion				= models.CharField(default='Institucion', max_length=30, blank=True)
	matricula				= models.CharField(default='Matricula', max_length=30, blank=True)
	is_doctor				= models.BooleanField(default=False)
	is_investigador			= models.BooleanField(default=True)
	cuenta 					= models.ForeignKey(Account, blank=True, null= True, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre + ' ' + self.apellido