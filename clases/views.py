from django.shortcuts import render
from .models import Clase,Alumno

# Create your views here.
def clases(request):
    data = {
        "alumnos":Clase.objects.all()
    }  
    return render(request, 'core/home.html',data)

def getalumnos(request):
    data = {
        "alumnos":Alumno.objects.all()
    }
    return render(request, 'core/lista_alumnos.html',data)


def veralumno (request, id):
    data = {
        "alumnos":Alumno.objects.filter(id = id)
    }
    return render(request, 'core/alumnos.html',data)

def ver_matriculados(request, id):
    a = Alumno.objects.filter(clases=id)   
    context = {
      'alumnos' : a
    }
    return render(request, 'core/matriculados.html', context)
