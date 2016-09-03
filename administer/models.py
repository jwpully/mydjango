from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CustomUser(models.Model):
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30, blank=True, null=False)
    last_name = models.CharField(max_length=30, blank=True, null=False)
    email = models.CharField(max_length=254, blank=False, null=False)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    username = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
        managed = False

    def __unicode__(self):
        return self.username