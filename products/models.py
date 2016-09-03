from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    code = models.CharField(max_length=64, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    active_flag = models.BooleanField()

    class Meta:
        db_table = 'cb_products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-active_flag', 'name']

    def __unicode__(self):
        return self.name
