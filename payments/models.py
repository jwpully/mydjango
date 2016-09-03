from __future__ import unicode_literals

from django.db import models
from accounts.models import Account

# Create your models here.
class Payment(models.Model):
    account = models.ForeignKey(Account, blank=False, null=False)
    amount = models.FloatField(blank=False, null=False)
    instrument_number = models.CharField(max_length=128, blank=False, null=False)
    memo = models.CharField(max_length=256, blank=True, null=True)
    payment_date = models.DateField(blank=False, null=False)
    postmark_date = models.DateField(blank=True, null=True)
    processed_date = models.DateField(auto_now_add=True, blank=True)
    type_code = models.CharField(max_length=8, blank=True, null=True)


    class Meta:
        db_table = 'cb_payments'
        verbose_name = 'Process Payment'
        verbose_name_plural = 'Process Payments'
        ordering = ['account']

    def __unicode__(self):
        return self.account.account_number

class PaymentHistory(models.Model):
    account = models.ForeignKey(Account, blank=False, null=False)
    amount = models.FloatField(blank=False, null=False)
    instrument_number = models.CharField(max_length=128, blank=False, null=False)
    memo = models.CharField(max_length=256, blank=True, null=True)
    payment_date = models.DateField(blank=False, null=False)
    postmark_date = models.DateField(blank=True, null=True)
    processed_date = models.DateField(auto_now_add=True, blank=True)
    type_code = models.CharField(max_length=8, blank=True, null=True)


    class Meta:
        db_table = 'cb_payments'
        verbose_name = 'Payment History'
        verbose_name_plural = 'Payment History'
        ordering = ['account']
        managed = False

    def __unicode__(self):
        return self.account.account_number