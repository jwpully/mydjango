# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('position', models.CharField(choices=[('President', 'President'), ('Vice President', 'Vice President'), ('Secretary', 'Secretary'), ('Treasurer', 'Treasurer'), ('Director', 'Director')], max_length=64)),
                ('start_term', models.DateField()),
                ('end_term', models.DateField()),
                ('start_role', models.DateField()),
                ('end_role', models.DateField()),
                ('active_flag', models.BooleanField()),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
                'db_table': 'cb_members',
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
            },
        ),
    ]
