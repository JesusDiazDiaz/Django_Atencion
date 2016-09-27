from django.contrib import admin
from .models import Paciente, Doctor, Especialidad, Consulta, Examen


# Register your models here.

@admin.register(Paciente)
class adminPasiente(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'cedula']


@admin.register(Especialidad)
class adminEspecialidad(admin.ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(Doctor)
class adminDoctro(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', ]


@admin.register(Consulta)
class consultaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'doctor', 'fecha']


@admin.register(Examen)
class examenAdmin(admin.ModelAdmin):
    list_display = [
        'paciente',
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
