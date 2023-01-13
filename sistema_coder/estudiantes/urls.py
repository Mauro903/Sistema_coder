from django.urls import path

from estudiantes.views import saludar, listar_estudiantes


urlpatterns = [
    path("saludar/",saludar,),
    path("lista/", listar_estudiantes),
]
