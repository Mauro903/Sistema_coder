from django.shortcuts import render, redirect
from django.urls import reverse 
from django.http import HttpResponse
from datetime import datetime
from estudiantes.models import Estudiantes, Profesor, Curso
from estudiantes.forms import CursoFormulario
from django.db.models import Q

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

def crear_curso_a_mano(request):
    """No la estamos usando"""
    if request.method == "POST":
        data = request.POST
        curso = Curso(nombre=data["nombre"], comision=data["comision"])
        curso.save()
        url_exitosa = reverse("listar_cursos")
        return redirect(url_exitosa)
    else:
        return render(
            request=request,
            template_name= 'estudiantes/formulario_curso_a_mano.html'  
        )

def crear_curso(request):
    """Usamos esta que es la PRO"""
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso(nombre=data["nombre"], comision=data["comision"])
            curso.save()
            url_exitosa = reverse("listar_cursos")
            return redirect(url_exitosa)
    else: #GET
        formulario = CursoFormulario()
    return render(
            request=request,
            template_name= 'estudiantes/formulario_curso.html',  
            context={"formulario": formulario},
            )

def buscar_curso(request):
    if request.method == "POST":
        data = request.POST
        cursos = Curso.objects.filter(
            Q(nombre__contains=data["busqueda"]) | Q(comision__exact=data["busqueda"])
        )

        contexto = {
            "cursos": cursos
        }
        return render(
            request=request, 
            template_name="estudiantes/Lista_cursos.html",
            context=contexto,
        )

