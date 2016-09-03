from __future__ import unicode_literals

from django.db import models
from accounts.models import Account, Product

# Create your models here.
class Charge(models.Model):
    account = models.ForeignKey(Account, blank=False, null=False)
    charge_num = models.IntegerField(blank=False, null=False)
    product = models.ForeignKey(Product, blank=False, null=False)
    amount = models.FloatField(blank=False, null=False)
    invoice_date = models.DateField(blank=False, null=False)
    due_date = models.DateField(blank=False, null=False)
    type_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'cb_charges'
        verbose_name = 'Add Charge'
        verbose_name_plural = 'Add Charges'
        ordering = ['invoice_date', 'account']

    def __unicode__(self):
        return self.account.account_number

class ChargeHistory(models.Model):
    account = models.ForeignKey(Account, blank=False, null=False)
    charge_num = models.IntegerField(blank=False, null=False)
    product = models.ForeignKey(Product, blank=False, null=False)
    amount = models.FloatField(blank=False, null=False)
    invoice_date = models.DateField(blank=False, null=False)
    due_date = models.DateField(blank=False, null=False)
    type_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'cb_charges'
        verbose_name = 'Charge History'
        verbose_name_plural = 'Charge History'
        ordering = ['invoice_date', 'account']
        managed = False

    def __unicode__(self):
        return self.account.account_number