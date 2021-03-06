from django.contrib import admin
from models import Account

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    fields = ['account_number', 'active_flag', 'created', 'deactivated', 'property']
    list_display = ('account_number', 'active_flag', 'property')
    ordering = ('-active_flag', 'account_number',)
    readonly_fields = ['account_number', 'created']
    search_fields = ['account_number']

admin.site.register(Account, AccountAdmin)
