# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('active_flag', models.BooleanField()),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'cb_products',
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
