# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 21:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readonly', '0002_auto_20160128_2104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerview',
            options={'managed': False, 'ordering': ['account'], 'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
    ]
