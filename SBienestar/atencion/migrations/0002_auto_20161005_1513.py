# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-05 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='antecedentes_paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='atencion.Antecedente'),
        ),
    ]