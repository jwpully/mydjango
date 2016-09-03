from __future__ import unicode_literals

from django.db import models
from django.db.models import Max
from products.models import Product
from properties.models import Property
import datetime

class GenerateAccount(models.Model):
    prefix = models.CharField(max_length=6, null=False, blank=False)
    suffix = models.CharField(max_length=4, null=False, blank=False)
    property = models.ForeignKey(Property, blank=False, null=False)

    class Meta:
        db_table = 'cb_gen_account_num_vw'
        verbose_name = 'Generate Account'
        verbose_name_plural = 'Generate Accounts'
        ordering = ['prefix', 'suffix']
        managed = False

class Account(models.Model):
    account_number = models.CharField(max_length=128, null=False, blank=True)
    active_flag = models.BooleanField()
    created = models.DateField(auto_now_add=True, blank=True)
    deactivated = models.DateField(blank=True, null=True)
    # default_product = models.ForeignKey(Product, blank=False, null=False, related_name='account_default_product')
    property = models.ForeignKey(Property, blank=False, null=False, related_name='account_property')

    class Meta:
        db_table = 'cb_accounts'
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        ordering = ['-active_flag', 'account_number']

    def __unicode__(self):
        return str(str(self.prefix) + str(self.suffix))


    #Overriding
    def save(self, *args, **kwargs):
        #check if the row with this hash already exists.
        if not self.pk:

            current_accounts = Account.objects.all().filter(property_id=self.property.id)
            for i, j in enumerate(current_accounts):
                this = None
                customer = None
                customerget = None
                this = Account.objects.get(pk=j.id)
                customer = DeactivateCustomer.objects.all().filter(account_id=this.id)
                for k, l in enumerate(customer):
                    customerget = None
                    customerget = DeactivateCustomer.objects.get(pk=l.id)
                    customerget.active_flag = False
                    customerget.save()
                this.active_flag = False
                this.deactivated = datetime.datetime.now()
                this.save()

            last_account = GenerateAccount.objects.all().filter(property_id=self.property.id).aggregate(Max('suffix'))
            prefix = GenerateAccount.objects.filter(property_id=self.property.id)[0]
            self.account_number = str(prefix.prefix) + str((int(last_account['suffix__max']) + 1)).zfill(4)
        super(Account, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.account_number

class DeactivateCustomer(models.Model):
    account = models.ForeignKey(Account, blank=False, null=False)
    active_flag = models.BooleanField()

    class Meta:
        db_table = 'cb_customers'
        managed = False

    def __unicode__(self):
        return self.account