from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Property(models.Model):
    number = models.CharField(max_length=6, blank=False, null=False)
    street = models.CharField(max_length=64, blank=False, null=False)
    section = models.CharField(max_length=8, blank=False, null=False)
    lot = models.CharField(max_length=8, blank=False, null=False)

    class Meta:
        db_table = 'cb_properties'
        verbose_name = 'property'
        verbose_name_plural = 'properties'
        ordering  = ['number', 'street', 'section', 'lot']

    def __unicode__(self):
        return str(str(self.number) + ' ' + str(self.street))
