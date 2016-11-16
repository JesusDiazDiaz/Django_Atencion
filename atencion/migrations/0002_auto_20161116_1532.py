# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-16 20:32
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='ciudad',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='departamento', chained_model_field='depto', on_delete=django.db.models.deletion.CASCADE, to='atencion.Ciudad'),
        ),
    ]