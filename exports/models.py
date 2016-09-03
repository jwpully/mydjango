from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Export(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    code = models.CharField(max_length=16, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=128, blank=False, null=False)
    group = models.CharField(max_length=128, blank=False, null=False)
    run = models.BooleanField()

    class Meta:
        db_table = 'cb_exports'
        verbose_name = 'Admin Export'
        verbose_name_plural = 'Admin Exports'

    def __unicode__(self):
        return self.name

class StringParameter(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    code = models.CharField(max_length=16, blank=False, null=False)
    parameter = models.CharField(max_length=128, blank=True, null=True)
    export = models.ForeignKey(Export, blank=False, null=False)

    class Meta:
        db_table = 'cb_export_string_parameter'
        verbose_name = 'Admin String Parameter'
        verbose_name_plural = 'Admin String Parameter'

    def __unicode__(self):
        return self.name

class DateParameter(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    code = models.CharField(max_length=16, blank=False, null=False)
    parameter = models.DateField(blank=False, null=False)
    export = models.ForeignKey(Export, blank=False, null=False)

    class Meta:
        db_table = 'cb_export_date_parameters'
        verbose_name = 'Admin Date Parameter'
        verbose_name_plural = 'Admin Date Parameter'

    def __unicode__(self):
        return self.name

class ExportUser(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    code = models.CharField(max_length=16, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=128, blank=False, null=False)
    group = models.CharField(max_length=128, blank=False, null=False)
    run = models.BooleanField()

    class Meta:
        db_table = 'cb_exports'
        verbose_name = 'Export'
        verbose_name_plural = 'Exports'
        managed = False

    def __unicode__(self):
        return self.name


class StringParameterUser(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    code = models.CharField(max_length=16, blank=False, null=False)
    parameter = models.CharField(max_length=128, blank=True, null=True)
    export = models.ForeignKey(ExportUser, blank=False, null=False)

    class Meta:
        db_table = 'cb_export_string_parameter'
        verbose_name = 'String Parameter'
        verbose_name_plural = 'String Parameter'
        managed = False

    def __unicode__(self):
        return self.name

class DateParameterUser(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    code = models.CharField(max_length=16, blank=False, null=False)
    parameter = models.DateField(blank=False, null=False)
    export = models.ForeignKey(ExportUser, blank=False, null=False)

    class Meta:
        db_table = 'cb_export_date_parameters'
        verbose_name = 'Date Parameter'
        verbose_name_plural = 'Date Parameter'
        managed = False

    def __unicode__(self):
        return self.name


