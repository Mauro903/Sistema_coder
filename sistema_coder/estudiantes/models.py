from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=64) #nombre = models.CharField(max_length=64, unique= True) asi con el unique que indica solo podes poner un nombre una vez
    comision = models.IntegerField() #Numerico
   # fecha_inicio = models.DateField(null=True)
  #Se puede poner unique_together para que no se repita una combinacion
    def __str__(self):
        return f"{self.nombre}, {self.comision}"


class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=True) #El null=True es para no tener que completarlo
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}" #Para que en el queryset, me diga directamente los strings de los objetos

class Profesor(models.Model):
    nombre = models.CharField(max_length=30) #Caracteres
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=True)
    profesion = models.CharField(max_length=128)
    bio = models.TextField(null=True) #Archivo de texto que no tiene limites

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_de_entrega = models.DateTimeField()
    is_approved = models.BooleanField(default=False)
    is_desapproved = models.BooleanField(default=False)

class Instituto(models.Model):
    nombre = models.CharField(max_length=256)