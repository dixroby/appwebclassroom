from django.db import models

class Clase(models.Model):
    nombre = models.CharField(max_length=200)
    Descripcion = models.TextField(max_length=200)
    disponibilidad = models.BooleanField(null=True)
    
    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    edad = models.IntegerField(null=True)
    activo = models.BooleanField(null=True)

    clases = models.ManyToManyField(Clase, related_name = 'estudiantes') 

    def __str__(self):
        return self.nombre