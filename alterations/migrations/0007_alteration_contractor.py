# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-05 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alterations', '0006_auto_20160831_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='alteration',
            name='contractor',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
