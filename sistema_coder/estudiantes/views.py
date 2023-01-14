from django.shortcuts import render, redirect
from django.urls import reverse 
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

def crear_curso(request):
    if request.method == "POST":
        data = request.POST
        curso = Curso(nombre=data["nombre"], comision=data["comision"])
        curso.save()
        url_exitosa = reverse("listar_cursos")
        return redirect(url_exitosa)
    else:
        return render(
            request=request,
            template_name= 'estudiantes/formulario_curso.html'  
        )