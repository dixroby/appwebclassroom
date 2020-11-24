from django.contrib import admin

from clases.models import Clase, Alumno

admin.site.register(Alumno)
admin.site.register(Clase)