# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-23 14:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20160504_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='default_product',
        ),
    ]