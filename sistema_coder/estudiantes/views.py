from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def saludar(request):
    return HttpResponse(f"Hola Soy Mauro Pisani y hoy es: {datetime.now()}")

def listar_estudiantes(request):
    return render(request=request, template_name="estudiantes/Lista_estudiantes.html")

# Create your views here.
