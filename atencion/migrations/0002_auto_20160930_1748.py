# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-30 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nacimiento',
            field=models.DateField(),
        ),
    ]
