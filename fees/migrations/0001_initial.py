# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('value', models.FloatField()),
                ('fee_type', models.CharField(choices=[('D', 'Dollar'), ('P', 'Percent')], max_length=64)),
                ('active_flag', models.BooleanField()),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'cb_fees',
                'verbose_name': 'Fee',
                'verbose_name_plural': 'Fees',
            },
        ),
    ]
