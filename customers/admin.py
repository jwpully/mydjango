from django.contrib import admin
from django import forms
from models import Customer, CustomerChange
from accounts.models import Account

# Register your models here.
class CustomCustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['account', 'customer_name', 'contact_first_name', 'contact_last_name', 'email', 'phone', 'fax', 'mobile', \
              'address_line_1', 'address_line_2', 'city', 'state', 'postal_code', 'country', \
              'customer_currency', 'owner_since', 'effective_date', 'active_flag']
    def __init__(self, *args, **kwargs):
        super(CustomCustomerModelForm, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = Account.objects.filter(active_flag=True)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('account', 'customer_name', 'active_flag')
    ordering = ('-active_flag', 'account',)
    search_fields = ['account__account_number', 'customer_name', 'contact_first_name', 'contact_last_name']
    form = CustomCustomerModelForm

admin.site.register(Customer, CustomerAdmin)


class CustomerChangeAdmin(admin.ModelAdmin):
    fields = ['account', 'customer_name', ('contact_first_name', 'contact_last_name'), 'email', ('phone', 'fax', 'mobile'), \
          ('address_line_1', 'address_line_2'), 'city', ('state', 'postal_code'), 'country', \
          'customer_currency', 'owner_since', 'effective_date', 'active_flag']
    list_display = ('account', 'customer_name', 'active_flag')
    ordering = ('-active_flag', 'account',)
    readonly_fields = ['account']
    search_fields = ['account__account_number', 'customer_name', 'contact_first_name', 'contact_last_name']

admin.site.register(CustomerChange, CustomerChangeAdmin)