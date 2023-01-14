from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from estudiantes.models import Estudiantes, Profesor, Curso

def inicio(request):
   
    return render(
        request=request, 
        template_name="estudiantes/iniciar.html",
        )

def listar_estudiantes(request):
    contexto = {
        "estudiantes": Estudiantes.objects.all()
    }
    return render(
        request=request, 
        template_name="estudiantes/Lista_estudiantes.html",
        context=contexto,
        )

def listar_profesores(request):
    contexto = {
        "profesores": Profesor.objects.all()
    }
    return render(
        request=request, 
        template_name="estudiantes/Lista_profesores.html",
        context=contexto,
        )



def listar_cursos(request):
    contexto = {
        "cursos": Curso.objects.all()
    }
    return render(
        request=request, 
        template_name="estudiantes/Lista_cursos.html",
        context=contexto,
        )

# Create your views here.
