# Web Page Prototype
## Introduction
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
Para instalar estas herramientas en el ambiente Conda, primero se deberá iniciar un ambiente virtual. Para esto se deberá utilizar la siguiente línea de comando
```
conda create -n portal1 python=3.12.3 pillow=11.0.0 psycopg2=2.9.9 sqlparse=0.5.2 tzdata=2024.a django=5.1.3
```
Debido a que el ambiente de Conda no cuenta con la herramienta Django-auto-logout, se deberá intalar la misma utilizando pip. Para esto, se debe utilizar el siguiente comando
```
pip install auto-logout
```

## Utilizando la pantalla de comando de Windows
* Python (versión 3.12.3)
* Django (versión 4.2.11)
* Asgiref (versión 3.8.1)
* Django-auto-logout (versión 0.5.1)
* Pillow (versión 11.0.0)
* Psycopg2 (versión 2.9.10)
* Sqlparse (versión 0.5.1)
* Tzdata (versión 2024.1)

```
then the command
```
