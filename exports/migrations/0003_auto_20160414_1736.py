# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-14 17:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exports', '0002_dateparameteruser_exportuser_stringparameteruser'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='stringparameteruser',
            table='cb_export_string_parameter',
        ),
    ]
