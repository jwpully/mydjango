from __future__ import unicode_literals

from django.db import models

# Create your models here.

FEETYPES = (
    ('D', 'Dollar')
    , ('P', 'Percent')
)

class Fee(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    code = models.CharField(max_length=64, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    value = models.FloatField(blank=False, null=False)
    fee_type = models.CharField(max_length=64, blank=False, null=False, choices=FEETYPES)
    active_flag = models.BooleanField()

    class Meta:
        db_table = 'cb_fees'
        verbose_name = 'Fee'
        verbose_name_plural = 'Fees'
        ordering = ['name']

    def __unicode__(self):
        return self.name

