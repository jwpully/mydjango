# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-04 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_customer_effective_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=128)),
                ('email', models.CharField(blank=True, max_length=128, null=True)),
                ('contact_first_name', models.CharField(max_length=128)),
                ('contact_last_name', models.CharField(max_length=128)),
                ('customer_currency', models.CharField(choices=[('D', 'US Dollar')], max_length=1)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('fax', models.CharField(blank=True, max_length=10, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.CharField(choices=[('USA', 'USA')], max_length=3)),
                ('state', models.CharField(choices=[('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'), ('California', 'California'), ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'), ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virginia', 'Virginia'), ('Washington', 'Washington'), ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming')], max_length=32)),
                ('address_line_1', models.CharField(max_length=128)),
                ('address_line_2', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(max_length=128)),
                ('postal_code', models.CharField(max_length=5)),
                ('owner_since', models.DateField()),
                ('effective_date', models.DateField(blank=True, null=True)),
                ('active_flag', models.BooleanField()),
            ],
            options={
                'ordering': ['account'],
                'verbose_name': 'Change Customer',
                'db_table': 'cb_customers',
                'managed': False,
                'verbose_name_plural': 'Change Customers',
            },
        ),
    ]
