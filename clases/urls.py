from django.urls import path
from .views import clases, getalumnos,   ver_matriculados, veralumno

urlpatterns = [
   path('', clases, name ="home"), 
   path('alumno/ver/<id>', ver_matriculados,name="ver_matriculados"),

   path('getalumnos/', getalumnos,name="getalumnos"),
   path('ver/<id>', veralumno,name="ver"),


   
   
]