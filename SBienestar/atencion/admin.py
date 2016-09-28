from django.contrib import admin
from .models import Paciente, Doctor, Especialidad, Consulta, Examen, Facultad, Programa, Eps, Religion, Pais, \
    Departamento, Ciudad


# Register your models here.
@admin.register(Facultad)
class FacultadAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
    ]


@admin.register(Programa)
class ProgramaAdmin(FacultadAdmin):
    pass


@admin.register(Eps)
class EpsAdmin(FacultadAdmin):
    pass


@admin.register(Pais)
class PaisAdmin(FacultadAdmin):
    pass


@admin.register(Departamento)
class DepartamentoAdmin(FacultadAdmin):
    pass


@admin.register(Ciudad)
class CiudadAdmin(FacultadAdmin):
    pass


@admin.register(Religion)
class ReligionAdmin(FacultadAdmin):
    pass


@admin.register(Paciente)
class PasienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'cedula']


@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'doctor']


@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    list_display = [
        'estatura',
        'peso',
        'FC',
        'FR',
        'temperatura',
        'orl',
        'piel_anexo',
        'ostio_muscular',
        'cabeza_cuello',
        'torax',
        'abdomen',
        'genito_urinario',
        'extremidades',
        'neurologico',
    ]
