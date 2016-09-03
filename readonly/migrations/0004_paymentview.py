# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readonly', '0003_auto_20160128_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(blank=True, max_length=128, null=True)),
                ('memo', models.CharField(blank=True, max_length=128, null=True)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('postmark_date', models.DateField(blank=True, null=True)),
                ('processed_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['payment_date'],
                'verbose_name': 'Payment History',
                'db_table': 'cb_dues_payments_vw',
                'managed': False,
                'verbose_name_plural': 'Payments History',
            },
        ),
    ]
