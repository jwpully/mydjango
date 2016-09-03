from __future__ import unicode_literals

from django.db import models
from accounts.models import Account

COUNTRY = (
    ('USA','USA'),
)
STATE = (
    ('Alabama', 'Alabama'), 
    ('Alaska', 'Alaska'), 
    ('Arizona', 'Arizona'), 
    ('Arkansas', 'Arkansas'), 
    ('California', 'California'), 
    ('Colorado', 'Colorado'), 
    ('Connecticut', 'Connecticut'), 
    ('Delaware', 'Delaware'), 
    ('Florida', 'Florida'), 
    ('Georgia', 'Georgia'), 
    ('Hawaii', 'Hawaii'), 
    ('Idaho', 'Idaho'), 
    ('Illinois', 'Illinois'), 
    ('Indiana', 'Indiana'), 
    ('Iowa', 'Iowa'), 
    ('Kansas', 'Kansas'), 
    ('Kentucky', 'Kentucky'), 
    ('Louisiana', 'Louisiana'), 
    ('Maine', 'Maine'), 
    ('Maryland', 'Maryland'), 
    ('Massachusetts', 'Massachusetts'), 
    ('Michigan', 'Michigan'), 
    ('Minnesota', 'Minnesota'), 
    ('Mississippi', 'Mississippi'), 
    ('Missouri', 'Missouri'), 
    ('Montana', 'Montana'), 
    ('Nebraska', 'Nebraska'), 
    ('Nevada', 'Nevada'), 
    ('New Hampshire', 'New Hampshire'), 
    ('New Jersey', 'New Jersey'), 
    ('New Mexico', 'New Mexico'), 
    ('New York', 'New York'), 
    ('North Carolina', 'North Carolina'), 
    ('North Dakota', 'North Dakota'), 
    ('Ohio', 'Ohio'), 
    ('Oklahoma', 'Oklahoma'), 
    ('Oregon', 'Oregon'), 
    ('Pennsylvania', 'Pennsylvania'), 
    ('Rhode Island', 'Rhode Island'), 
    ('South Carolina', 'South Carolina'), 
    ('South Dakota', 'South Dakota'), 
    ('Tennessee', 'Tennessee'), 
    ('Texas', 'Texas'), 
    ('Utah', 'Utah'), 
    ('Vermont', 'Vermont'), 
    ('Virginia', 'Virginia'), 
    ('Washington', 'Washington'), 
    ('West Virginia', 'West Virginia'), 
    ('Wisconsin', 'Wisconsin'), 
    ('Wyoming', 'Wyoming'), 
)

CURRENCY = (
    ('D', 'US Dollar'),
)

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=128, blank=False, null=False)
    email = models.CharField(max_length=128, blank=True, null=True)
    contact_first_name = models.CharField(max_length=128, blank=False, null=False)
    contact_last_name = models.CharField(max_length=128, null=False, blank=False)
    customer_currency = models.CharField(max_length=1, blank=False, null=False, choices=CURRENCY)
    account = models.ForeignKey(Account, blank=False, null=False)
    phone = models.CharField(max_length=10, blank=True, null=True)
    fax = models.CharField(max_length=10, blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=3, blank=False, null=False, choices=COUNTRY)
    state = models.CharField(max_length=32, blank=False, null=False, choices=STATE)
    address_line_1 = models.CharField(max_length=128, blank=False, null=False)
    address_line_2 = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=128, blank=False, null=False)
    postal_code = models.CharField(max_length=5, blank=False, null=False)
    owner_since = models.DateField(blank=False, null=False)
    effective_date = models.DateField(blank=True, null=True)
    active_flag = models.BooleanField()

    class Meta:
        db_table = 'cb_customers'
        verbose_name = 'Add Customer'
        verbose_name_plural = 'Add Customers'
        ordering = ['account']

    def __unicode__(self):
        return self.customer_name

class CustomerChange(models.Model):
    customer_name = models.CharField(max_length=128, blank=False, null=False)
    email = models.CharField(max_length=128, blank=True, null=True)
    contact_first_name = models.CharField(max_length=128, blank=False, null=False)
    contact_last_name = models.CharField(max_length=128, null=False, blank=False)
    customer_currency = models.CharField(max_length=1, blank=False, null=False, choices=CURRENCY)
    account = models.ForeignKey(Account, blank=False, null=False)
    phone = models.CharField(max_length=10, blank=True, null=True)
    fax = models.CharField(max_length=10, blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=3, blank=False, null=False, choices=COUNTRY)
    state = models.CharField(max_length=32, blank=False, null=False, choices=STATE)
    address_line_1 = models.CharField(max_length=128, blank=False, null=False)
    address_line_2 = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=128, blank=False, null=False)
    postal_code = models.CharField(max_length=5, blank=False, null=False)
    owner_since = models.DateField(blank=False, null=False)
    effective_date = models.DateField(blank=True, null=True)
    active_flag = models.BooleanField()

    class Meta:
        db_table = 'cb_customers'
        verbose_name = 'Change Customer'
        verbose_name_plural = 'Change Customers'
        ordering = ['account']
        managed = False

    def __unicode__(self):
        return self.customer_name