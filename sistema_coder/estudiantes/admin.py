from django.contrib import admin

# Register your models here.


from estudiantes.models import	Curso, Estudiantes, Profesor, Entregable, Instituto

admin.site.register(Estudiantes)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Entregable)
admin.site.register(Instituto)
