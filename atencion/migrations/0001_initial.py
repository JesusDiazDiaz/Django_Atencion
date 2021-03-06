# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-17 19:26
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Antecedente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo', models.CharField(blank=True, choices=[('Personal', 'Personal'), ('Familiar', 'Familiar')], max_length=8, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Cuidad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_diagnostico', models.CharField(max_length=10)),
                ('fecha', models.DateField(auto_now=True)),
                ('conducta', models.TextField(blank=True, null=True)),
                ('recomendaciones', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctores',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Enfermedad',
                'verbose_name_plural': 'Enfermedades',
            },
        ),
        migrations.CreateModel(
            name='Eps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='ExamenFisico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatura', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('FC', models.IntegerField()),
                ('FR', models.IntegerField()),
                ('temperatura', models.IntegerField()),
                ('cabeza_cuello', models.CharField(blank=True, default='Normal', max_length=100)),
                ('orl', models.CharField(blank=True, default='Normal', max_length=100)),
                ('torax', models.CharField(blank=True, default='Normal', max_length=100)),
                ('abdomen', models.CharField(blank=True, default='Normal', max_length=100)),
                ('genito_urinario', models.CharField(blank=True, default='Normal', max_length=100)),
                ('osteo_muscular', models.CharField(blank=True, default='Normal', max_length=100)),
                ('piel_anexo', models.CharField(blank=True, default='Normal', max_length=100)),
                ('extremidades', models.CharField(blank=True, default='Normal', max_length=100)),
                ('neurologico', models.CharField(blank=True, default='Normal', max_length=100)),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atencion.Consulta')),
            ],
            options={
                'verbose_name': 'Historia clinica',
                'verbose_name_plural': 'Historias clinicas',
            },
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Facultad',
                'verbose_name_plural': 'Facultades',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=50, unique=True)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('edad', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.BigIntegerField()),
                ('tipo_sangre', models.CharField(choices=[('AB+', 'AB+'), ('AB-', 'AB-'), ('A+', 'A-'), ('B+', 'B-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3)),
                ('fecha_nacimiento', models.DateField(default='1900-12-30')),
                ('estado_civil', models.CharField(choices=[('Soltero', 'Soltero/a'), ('Casado', 'Casado/a'), ('Viudo', 'Viudo/a')], max_length=7)),
                ('ocupacion', models.CharField(max_length=50)),
                ('vinculacion', models.CharField(choices=[('Estudiante', 'Estudiante'), ('Funcionario', 'Funcionario'), ('Egresado', 'Egresado'), ('Visitante', 'Visitante')], max_length=12)),
                ('direccion', models.CharField(max_length=50)),
                ('ciudad', smart_selects.db_fields.ChainedForeignKey(chained_field='departamento', chained_model_field='depto', on_delete=django.db.models.deletion.CASCADE, to='atencion.Ciudad')),
                ('departamento', smart_selects.db_fields.ChainedForeignKey(chained_field='pais', chained_model_field='pais', on_delete=django.db.models.deletion.CASCADE, to='atencion.Departamento')),
                ('eps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atencion.Eps')),
                ('facultad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='atencion.Facultad')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'pais',
                'verbose_name_plural': 'paises',
            },
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atencion.Facultad')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Religion',
                'verbose_name_plural': 'Religiones',
            },
        ),
        migrations.AddField(
            model_name='paciente',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atencion.Pais'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='programa',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='facultad', chained_model_field='facultad', on_delete=django.db.models.deletion.CASCADE, to='atencion.Programa'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='religion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atencion.Religion'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='especialidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atencion.Especialidad'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atencion.Pais'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atencion.Doctor'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='motivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atencion.Enfermedad'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atencion.Paciente'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='depto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atencion.Departamento'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atencion.Paciente'),
        ),
        migrations.AlterUniqueTogether(
            name='paciente',
            unique_together=set([('nombre', 'apellido', 'cedula')]),
        ),
    ]
