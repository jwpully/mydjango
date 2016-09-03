# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 19:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('instrument_number', models.CharField(max_length=128)),
                ('memo', models.CharField(blank=True, max_length=256, null=True)),
                ('payment_date', models.DateField()),
                ('postmark_date', models.DateField(blank=True, null=True)),
                ('processed_date', models.DateField(auto_now_add=True)),
                ('type_code', models.CharField(blank=True, max_length=8, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
            options={
                'ordering': ['account'],
                'db_table': 'cb_payments',
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]