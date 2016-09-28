from django.db import models


# Create your models here.

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
    telefono = models.CharField(max_length=50)

    class Meta:
        abstract = True
        unique_together = ['nombre', 'apellido', 'cedula']

    def __str__(self):
        return '{0} {1}'.format(self.nombre, self.apellido)

    def nombre_completo(self):
        return self.__str__()


class Paciente(BasePersona):
    facultad = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    procedencia = models.CharField(max_length=50)
    residencia = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    vinculacion = models.CharField(max_length=50)
    ocupacion = models.CharField(max_length=50)
    eps = models.CharField(max_length=50)


class PropiedadNombre(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Pais(PropiedadNombre):
    pass


class Departamento(PropiedadNombre):
    pais = models.ForeignKey(Pais)


class Ciudad(PropiedadNombre):
    depto = models.ForeignKey(Departamento)


class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.nombre


class Doctor(BasePersona):
    especialidad = models.ForeignKey(Especialidad)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctores'

    def __str__(self):
        return '{0} {1} - Especialidad: {2}'.format(self.nombre, self.apellido, self.especialidad)


class Consulta(models.Model):
    doctor = models.ForeignKey(Doctor)
    paciente = models.ForeignKey(Paciente)

    # class Meta:
    #    unique_together = ['doctor', 'paciente']

    def __str__(self):
        return self.paciente.nombre


class Examen(models.Model):
    consultaP = models.ForeignKey(Consulta)
    fecha = models.DateTimeField()
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
        verbose_name = 'Examen'
        verbose_name_plural = 'Examenes'

    def __str__(self):
        return 'Examen de {0}'.format(self.paciente)
