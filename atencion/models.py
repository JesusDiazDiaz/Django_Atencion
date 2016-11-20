from django.contrib.auth.models import User
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

class BasePersona(models.Model):
    genero = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=50, unique=True)
    sexo = models.CharField(max_length=1, choices=genero)
    edad = models.IntegerField()
    email = models.EmailField(unique=True)
    telefono = models.BigIntegerField()

    class Meta:
        abstract = True
        unique_together = ['nombre', 'apellido', 'cedula']

    def __str__(self):
        return '{0} {1}'.format(self.nombre, self.apellido)

    def nombre_completo(self):
        return self.__str__()


class PropiedadNombre(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        abstract = True


class Eps(PropiedadNombre):
    class Meta:
        verbose_name = 'EPS'
        verbose_name_plural = 'EPS'


class Facultad(PropiedadNombre):
    class Meta:
        verbose_name_plural = 'Facultades'
        verbose_name = 'Facultad'


class Programa(PropiedadNombre):
    facultad = models.ForeignKey(Facultad)


class Religion(PropiedadNombre):
    class Meta:
        verbose_name_plural = 'Religiones'
        verbose_name = 'Religion'


class Pais(PropiedadNombre):
    class Meta:
        verbose_name = 'pais'
        verbose_name_plural = 'paises'


class Departamento(PropiedadNombre):
    pais = models.ForeignKey(Pais)


class Ciudad(PropiedadNombre):
    depto = models.ForeignKey(Departamento)

    class Meta:
        verbose_name_plural = 'Ciudades'
        verbose_name = 'Cuidad'


class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.nombre


class Paciente(BasePersona):
    tipo_vinculacion = (
        ('Estudiante', 'Estudiante'),
        ('Funcionario', 'Funcionario'),
        ('Egresado', 'Egresado'),
        ('Visitante', 'Visitante'),
    )
    estadoC = (
        ('Soltero', 'Soltero/a'),
        ('Casado', 'Casado/a'),
        ('Viudo', 'Viudo/a'),
    )
    sangre = (
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('A+', 'A-'),
        ('B+', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    )
    tipo_sangre = models.CharField(max_length=3, choices=sangre)
    fecha_nacimiento = models.DateField(default="1990-12-30")
    estado_civil = models.CharField(max_length=7, choices=estadoC)
    ocupacion = models.CharField(max_length=50)
    vinculacion = models.CharField(max_length=12, choices=tipo_vinculacion)
    facultad = models.ForeignKey(Facultad, blank=True, null=True)
    programa = ChainedForeignKey(
        Programa,
        chained_field='facultad',
        chained_model_field='facultad'
    )
    eps = models.ForeignKey(Eps)
    religion = models.ForeignKey(Religion)
    #Smart
    pais = models.ForeignKey(Pais)
    departamento = ChainedForeignKey(
        Departamento,
        chained_field='pais',
        chained_model_field='pais'
    )
    ciudad = ChainedForeignKey(
        Ciudad,
        chained_field='departamento',
        chained_model_field='depto'
    )
    direccion = models.CharField(max_length=50)


class Antecedente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo_Antecedestes = (
        ('Personal', 'Personal'),
        ('Familiar', 'Familiar')
    )
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=8, choices=tipo_Antecedestes)
    descripcion = models.TextField(blank=True, null=True)



class Doctor(User):
    especialidad = models.ForeignKey(Especialidad)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctores'


class Enfermedad(PropiedadNombre):
    class Meta:
        verbose_name_plural = 'Enfermedades'
        verbose_name = 'Enfermedad'


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor)
    motivo = models.ForeignKey(Enfermedad)
    #motivo = models.CharField(max_length=200)
    cod_diagnostico = models.CharField(max_length=10)
    fecha = models.DateField(auto_now=True, auto_now_add=False)
    conducta = models.TextField(blank=True, null=True)
    recomendaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'Consulta de {0}'.format(self.paciente.nombre_completo())


class ExamenFisico(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    #enfermedad = models.ForeignKey(Enfermedad)
    # examenes
    estatura = models.IntegerField()
    peso = models.IntegerField()
    FC = models.IntegerField()
    FR = models.IntegerField()
    temperatura = models.IntegerField()
    cabeza_cuello = models.CharField(max_length=100, blank=True, default="Normal")
    orl = models.CharField(max_length=100, blank=True, default="Normal")
    torax = models.CharField(max_length=100, blank=True, default="Normal")
    abdomen = models.CharField(max_length=100, blank=True, default="Normal")
    genito_urinario = models.CharField(max_length=100, blank=True, default="Normal")
    osteo_muscular = models.CharField(max_length=100, blank=True, default="Normal")
    piel_anexo = models.CharField(max_length=100, blank=True, default="Normal")
    extremidades = models.CharField(max_length=100, blank=True, default="Normal")
    neurologico = models.CharField(max_length=100, blank=True, default="Normal")

    class Meta:
        verbose_name = 'Historia clinica'
        verbose_name_plural = 'Historias clinicas'

    def __str__(self):
        return 'Historia clinica de {0}'.format(self.paciente.nombre_completo())
