from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=64)
    comision = models.IntegerField() #Numerico


class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30) #Caracteres
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length=128)
    bio = models.TextField() #Archivo de texto que no tiene limites

class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_de_entrega = models.DateTimeField()
    is_approved = models.BooleanField(default=False)
    is_desapproved = models.BooleanField(default=False)
