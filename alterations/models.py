from __future__ import unicode_literals

from django.db import models
from accounts.models import Account, Property

# Create your models here.

Status = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Denied', 'Denied'),
)

Builder = (
    ('contractor', 'Contractor')
    , ('homeowner', 'Home Owner')
)

class Alteration(models.Model):
    email = models.CharField(max_length=128, blank=True, null=True)
    fence = models.BooleanField(blank=True)
    shed = models.BooleanField(blank=True)
    pool = models.BooleanField(blank=True)
    room = models.BooleanField(blank=True)
    driveway = models.BooleanField(blank=True)
    garage = models.BooleanField(blank=True)
    deck = models.BooleanField(blank=True)
    other = models.BooleanField(blank=True)
    structureother = models.TextField(blank=True, null=True)
    builder = models.CharField(max_length=32, blank=True, null=True, choices=Builder)
    description = models.TextField(blank=False, null=False)
    size = models.CharField(max_length=64, blank=True, null=True)
    roof = models.CharField(max_length=64, blank=True, null=True)
    cost = models.CharField(max_length=64, blank=True, null=True)
    completion = models.CharField(max_length=64, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    file1 = models.FileField(blank=True, null=True)
    file2 = models.FileField(blank=True, null=True)
    file3 = models.FileField(blank=True, null=True)
    property = models.ForeignKey(Property, blank=False, null=False)
    status = models.CharField(max_length=64, blank=False, null=False, choices=Status, default='Pending')
    processed = models.DateField(auto_now_add=True, blank=True, null=True)
    requested = models.DateField(blank=False, null=False, auto_now_add=True)
    finalized = models.DateField(blank=True, null=True)
    account = models.ForeignKey(Account, blank=False, null=False)
    waiver = models.BooleanField()
    reason = models.TextField(blank=True, null=True)
    special_instructions = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'cb_alterations'
        verbose_name = 'Alteration'
        verbose_name_plural = 'Alterations'
        ordering = ['requested', 'account']

    def __unicode__(self):
        return str(self.account)
        #return str(str(self.property.number) + ' ' + str(self.property.street) + ' ' + str(self.account.account_number))

