# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AtencionConsulta(models.Model):
    fecha = models.DateTimeField()
    doctor = models.ForeignKey('AtencionDoctor', models.DO_NOTHING)
    paciente = models.ForeignKey('AtencionPaciente', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'atencion_consulta'
        unique_together = (('doctor', 'paciente', 'fecha'),)


class AtencionDoctor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(unique=True, max_length=50)
    sexo = models.CharField(max_length=25)
    edad = models.IntegerField()
    email = models.CharField(unique=True, max_length=254)
    telefono = models.CharField(max_length=50)
    especialidad = models.ForeignKey('AtencionEspecialidad', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'atencion_doctor'


class AtencionEspecialidad(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'atencion_especialidad'


class AtencionExamen(models.Model):
    paciente = models.ForeignKey(AtencionConsulta, models.DO_NOTHING, primary_key=True)
    estatura = models.IntegerField()
    peso = models.IntegerField()
    fc = models.IntegerField(db_column='FC')  # Field name made lowercase.
    fr = models.IntegerField(db_column='FR')  # Field name made lowercase.
    temperatura = models.IntegerField()
    orl = models.CharField(max_length=100)
    piel_anexo = models.CharField(max_length=100)
    ostio_muscular = models.CharField(max_length=100)
    cabeza_cuello = models.CharField(max_length=100)
    torax = models.CharField(max_length=100)
    abdomen = models.CharField(max_length=100)
    genito_urinario = models.CharField(max_length=100)
    extremidades = models.CharField(max_length=100)
    neurologico = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'atencion_examen'


class AtencionPaciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(unique=True, max_length=50)
    sexo = models.CharField(max_length=25)
    edad = models.IntegerField()
    email = models.CharField(unique=True, max_length=254)
    telefono = models.CharField(max_length=50)
    facultad = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    procedencia = models.CharField(max_length=50)
    residencia = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    vinculacion = models.CharField(max_length=50)
    ocupacion = models.CharField(max_length=50)
    eps = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'atencion_paciente'
        unique_together = (('nombre', 'apellido', 'cedula'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
