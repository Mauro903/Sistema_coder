from django.urls import path

from estudiantes.views import saludar, listar_estudiantes, listar_profesores


urlpatterns = [
    path("saludar/",saludar,),
    path("lista-alumnos/", listar_estudiantes, name="listar_alumnos"), #El name= sirve para que si cambia la url puedo seguir teniendo el mismo nombre en el html
    path("lista-profesores/", listar_profesores, name="listar_profesores"),
]
