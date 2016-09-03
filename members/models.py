from __future__ import unicode_literals

from django.db import models

# Create your models here.

Positions = (
    ('President', 'President'),
    ('Vice President', 'Vice President'),
    ('Secretary', 'Secretary'),
    ('Treasurer', 'Treasurer'),
    ('Director', 'Director')
)

class Member(models.Model):
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128, blank=False, null=False)
    position = models.CharField(max_length=64, blank=False, null=False, choices=Positions)
    start_term = models.DateField(blank=False, null=False)
    end_term = models.DateField(blank=False, null=False)
    start_role = models.DateField(blank=False, null=False)
    end_role = models.DateField(blank=False, null=False)
    active_flag = models.BooleanField()
    duty = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'cb_members'
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
        ordering = ['last_name', 'first_name']

    def __unicode__(self):
        return str(str(self.first_name) + ' ' + str(self.last_name))



