from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Process(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    code = models.CharField(max_length=16, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=128, blank=False, null=False)
    group = models.CharField(max_length=128, blank=False, null=False)
    run = models.BooleanField()

    class Meta:
        db_table = 'cb_processes'
        verbose_name = 'Admin Process'
        verbose_name_plural = 'Admin Processes'

    def __unicode__(self):
        return self.name

class StringParameter(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    code = models.CharField(max_length=16, blank=False, null=False)
    parameter = models.CharField(max_length=128, blank=True, null=True)
    process = models.ForeignKey(Process, blank=False, null=False)

    class Meta:
        db_table = 'cb_string_parameters'
        verbose_name = 'Admin String Parameter'
        verbose_name_plural = 'Admin String Parameter'

    def __unicode__(self):
        return self.name

class DateParameter(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    code = models.CharField(max_length=16, blank=False, null=False)
    parameter = models.DateField(blank=True, null=True)
    process = models.ForeignKey(Process, blank=False, null=False)

    class Meta:
        db_table = 'cb_date_parameters'
        verbose_name = 'Admin Date Parameter'
        verbose_name_plural = 'Admin Date Parameter'

    def __unicode__(self):
        return self.name



class ProcessUser(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    code = models.CharField(max_length=16, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=128, blank=False, null=False)
    group = models.CharField(max_length=128, blank=False, null=False)
    run = models.BooleanField()

    class Meta:
        db_table = 'cb_processes'
        verbose_name = 'Process'
        verbose_name_plural = 'Processes'
        managed = False

    def __unicode__(self):
        return self.name


class StringParameterUser(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    code = models.CharField(max_length=16, blank=False, null=False)
    parameter = models.CharField(max_length=128, blank=True, null=True)
    process = models.ForeignKey(ProcessUser, blank=False, null=False)

    class Meta:
        db_table = 'cb_string_parameters'
        verbose_name = 'String Parameter'
        verbose_name_plural = 'String Parameter'
        managed = False

    def __unicode__(self):
        return self.name

class DateParameterUser(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    code = models.CharField(max_length=16, blank=False, null=False)
    parameter = models.DateField(blank=True, null=True)
    process = models.ForeignKey(ProcessUser, blank=False, null=False)

    class Meta:
        db_table = 'cb_date_parameters'
        verbose_name = 'Date Parameter'
        verbose_name_plural = 'Date Parameter'
        managed = False

    def __unicode__(self):
        return self.name

