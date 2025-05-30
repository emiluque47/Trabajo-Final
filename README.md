# Prototipo de Portal Web
## Introducción
En este documento se estará dando una breve descripción del proyecto, sus características y modo de instalación. Este proyecto se encargó de desarrollar el prototipo de una plataforma web que tenga las siguientes funcionalidades:<br>
+ Carga de datos de pacientes
+ Manejo de datos de pacientes
+ Carga de estudios
+ Solicitud de simulación
+ Manejo de solicitudes de simulación
+ Carga de resultados de simulación
+ Manejo de resultados de simulación <br>

Si bien una explicación sobre el manejo de esta herramienta está fuera del alcance de este documento

## Cómo instalar
En esta sección se estarán explicando los pasos necesarios para descargar y correr el proyecto en un ambiente local.<br>
Para eso se dividirá en dos secciones, la primera explicará la instalación de las herramientas usando el ambiente Anaconda, y la segunda será utilizando la pantalla de comando de windows.
Para esta herramienta se utilizaron las siguientes librerías:
* Python
* Django
* Asgiref 
* Django-auto-logout 
* Pillow 
* Psycopg2
* Sqlparse
* Tzdata<br>

Dependiendo del ambiente utilizadon para la instalación se deberán utilizar ciertas versiones de estas herramientas, pero en dichos casos se espcecificará la versión utilizada.<br>
## Utilizando Conda
Para instalar estas herramientas en el ambiente Conda, primero se deberá iniciar un ambiente virtual. Para esto se deberá iniciar Powershell desde el Anaconda Navigator y navegar hasta la carpeta del proyecto. Una vez ahí, se debe utilizar la siguiente línea de comando
```
conda create -n portal1 python=3.12.3 pillow=11.0.0 psycopg2=2.9.9 sqlparse=0.5.2 tzdata django=5.1.3
```
Debido a que el ambiente de Conda no cuenta con la herramienta Django-auto-logout, se deberá intalar la misma utilizando pip. Para esto, se deben seguir los siguientes pasos:

1. Iniciar el ambiente virtual utilizando el siguiente comando
   ```
   conda activate portal1
   ```
2. Una vez iniciado el ambiente virtual se deberá instalar la herramienta con el siguiente commando
   ```
   pip install auto-logout
   ```
Con estas herramientas se finalizaron los preparativos para iniciar el servidor del prototipo. Ahora, se deberá navegar hasta el directorio src en la ventana Powershell y utilizar el siguiente comando

```
python manage.py runserver
```
Con estos preparativos listos, el prototipo puede ser accedido desde un navegador web accediendo a 127.0.0.1:8000

## Utilizando la pantalla de comando de Windows
Para la pantalla de comando de windows se utilizarán las mismas herramientas, pero se deberán instalar utilizando el comando pip. Para esto se deberá navegar hasta la carpeta Scripts del repositorio y abrir la pantalla de commando de windows.<br>
Una vez que esté abierta la pantalla de commando se deberá abrir el archivo de activación del ambiente virtual con el siguiente comando
```
activate
```
Una vez que se haya activado el ambiente virtual, se debe navegar hasta la carpeta src y utilizar el siguiente comando
```
pip install -r requirement.txt
```
Este comando estará instalando las siguientes versiones de las herramientas
* Python (versión 3.12.3)
* Django (versión 4.2.11)
* Asgiref (versión 3.8.1)
* Django-auto-logout (versión 0.5.1)
* Pillow (versión 11.0.0)
* Psycopg2 (versión 2.9.10)
* Sqlparse (versión 0.5.1)
* Tzdata (versión 2024.1)
  
