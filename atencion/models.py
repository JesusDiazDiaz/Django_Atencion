from django.contrib.auth.models import User
from django.db import models


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
    pass


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
    #tipo de sangre
    vinculacion = models.CharField(max_length=12, choices=tipo_vinculacion)
    estado_civil = models.CharField(max_length=7, choices=estadoC)
    nacimiento = models.DateField(default="1900-12-30")
    ocupacion = models.CharField(max_length=50)
    facultad = models.ForeignKey(Facultad, blank=True, null=True)
    programa = models.ForeignKey(Programa, blank=True, null=True)
    eps = models.ForeignKey(Eps)
    religion = models.ForeignKey(Religion)
    ciudad = models.ForeignKey(Ciudad)
    departamento = models.ForeignKey(Departamento)
    pais = models.ForeignKey(Pais)
    direccion = models.CharField(max_length=50)


class Antecedente(models.Model):
    paciente = models.ForeignKey(Paciente)
    tipo_Antecedestes = (
        ('P', 'Personal'),
        ('F', 'Familiar')
    )
    nombre = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True)
    tipo = models.CharField(max_length=1, choices=tipo_Antecedestes, null=True, blank=True)


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
    paciente = models.ForeignKey(Paciente)
    doctor = models.ForeignKey(Doctor)
    motivo = models.CharField(max_length=200)
    cod_diagnostico = models.CharField(max_length=10)
    fecha = models.DateField(auto_now=True, auto_now_add=False)
    conducta = models.TextField(blank=True, null=True)
    recomendaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'Consulta de {0}'.format(self.paciente.nombre_completo())


class ExamenFisico(models.Model):
    consulta = models.ForeignKey(Consulta)
    enfermedad = models.ForeignKey(Enfermedad)
    # examenes
    estatura = models.IntegerField()
    peso = models.IntegerField()
    FC = models.IntegerField()
    FR = models.IntegerField()
    temperatura = models.IntegerField()
    orl = models.CharField(max_length=100, blank=True, default="Normal")
    piel_anexo = models.CharField(max_length=100, blank=True, default="Normal")
    ostio_muscular = models.CharField(max_length=100, blank=True, default="Normal")
    cabeza_cuello = models.CharField(max_length=100, blank=True, default="Normal")
    torax = models.CharField(max_length=100, blank=True, default="Normal")
    abdomen = models.CharField(max_length=100, blank=True, default="Normal")
    genito_urinario = models.CharField(max_length=100, blank=True, default="Normal")
    extremidades = models.CharField(max_length=100, blank=True, default="Normal")
    neurologico = models.CharField(max_length=100, blank=True, default="Normal", )

    class Meta:
        verbose_name = 'Historia clinica'
        verbose_name_plural = 'Historias clinicas'

    def __str__(self):
        return 'Historia clinica de {0}'.format(self.paciente.nombre_completo())