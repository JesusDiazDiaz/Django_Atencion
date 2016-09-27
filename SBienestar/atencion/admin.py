from django.contrib import admin
from .models import Paciente, Doctor, Especialidad, Consulta, Examen


# Register your models here.

@admin.register(Paciente)
class PasienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'cedula']


@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', ]


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
