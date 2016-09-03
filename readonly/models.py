from __future__ import unicode_literals

from django.db import models
from accounts.models import Account

# Create your models here.

class CustomerView(models.Model):
    contact_name = models.CharField(max_length=128, blank=False, null=False)
#    account_number = models.CharField(max_length=128, blank=False, null=False)
    account = models.ForeignKey(Account, blank=False, null=False)
    balance = models.FloatField(blank=False, null=False)
    contact_address = models.CharField(max_length=256, blank=False, null=False)
    total_charges = models.CharField(max_length=64, blank=False, null=False)

    class Meta:
        db_table = 'cb_customer_summary_vw'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['account']
        managed = False

    def save(self):
        return True

    def __unicode__(self):
        return str(str(self.contact_name) + ' - ' + str(self.balance))

class PaymentView(models.Model):
    amount = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=128, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    postmark_date = models.DateField(blank=True, null=True)
    processed_date = models.DateField(blank=True, null=True)
    customer = models.ForeignKey(CustomerView, blank=False, null=False)

    class Meta:
        db_table = 'cb_dues_payments_vw'
        verbose_name = 'Payment History'
        verbose_name_plural = 'Payments History'
        ordering = ['payment_date']
        managed = False

    def save(self):
        return True

    def __unicode__(self):
        return str(str(self.payment_date) + ' - ' + str(self.amount))

