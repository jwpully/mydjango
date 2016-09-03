from django.contrib import admin
from django import forms
from django.db.models import Max
from models import Charge, ChargeHistory
from accounts.models import Account
from products.models import Product

# Register your models here.
class CustomChargeModelForm(forms.ModelForm):
    class Meta:
        model = Charge
        fields = ['account', 'charge_num', 'product', 'amount', 'invoice_date', 'due_date', 'type_code']

    def __init__(self, *args, **kwargs):
        super(CustomChargeModelForm, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = Account.objects.filter(active_flag=True)
        self.fields['product'].queryset = Product.objects.filter(active_flag=True)
        last_charge_num = Charge.objects.all().aggregate(Max('charge_num'))
        self.fields['charge_num'].initial = (int(last_charge_num['charge_num__max']) + 1)
        self.fields['charge_num'].widget.attrs['readonly'] = True


class ChargeAdmin(admin.ModelAdmin):
    list_display = ('account', 'charge_num', 'product', 'invoice_date')
    ordering = ('invoice_date','account')
    search_fields = ['account__account_number',]
    form = CustomChargeModelForm

admin.site.register(Charge, ChargeAdmin)

class ChargeHistoryAdmin(admin.ModelAdmin):
    fields = ['account', 'charge_num', 'product', 'amount', 'invoice_date', 'due_date', 'type_code']
    list_display = ('account', 'charge_num', 'product', 'invoice_date')
    ordering = ('invoice_date','account')
    readonly_fields = ['account', 'charge_num', 'product', 'invoice_date', 'due_date']
    search_fields = ['account__account_number',]

admin.site.register(ChargeHistory, ChargeHistoryAdmin)
