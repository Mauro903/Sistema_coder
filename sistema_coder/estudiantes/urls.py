from django.urls import path

from estudiantes.views import inicio, listar_estudiantes, listar_profesores


urlpatterns = [
    path("inicio/",inicio, name="iniciar"),
    path("alumnos/", listar_estudiantes, name="listar_alumnos"), #El name= sirve para que si cambia la url puedo seguir teniendo el mismo nombre en el html
    path("profesores/", listar_profesores, name="listar_profesores"),
]
