# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-27 18:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ['number', 'street', 'section', 'lot'], 'verbose_name': 'property', 'verbose_name_plural': 'properties'},
        ),
    ]
