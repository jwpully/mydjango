from django.contrib import admin
from django import forms
from models import Payment, PaymentHistory
from accounts.models import Account
# Register your models here.


#Create custom form with specific queryset:
class CustomPaymentModelForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['account', 'amount', 'instrument_number', 'memo', 'type_code', 'payment_date', 'postmark_date']
    def __init__(self, *args, **kwargs):
        super(CustomPaymentModelForm, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = Account.objects.filter(active_flag=True)# or something else

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'type_code', 'payment_date', 'postmark_date')
    ordering = ('payment_date','account')
    search_fields = ['account__account_number', 'instrument_number', 'amount', 'memo']
    form = CustomPaymentModelForm

admin.site.register(Payment, PaymentAdmin)

class PaymentHistoryAdmin(admin.ModelAdmin):
    fields = ['account', 'amount', 'instrument_number', 'memo', 'type_code', 'payment_date', 'postmark_date', 'processed_date']
    list_display = ('account', 'amount', 'type_code', 'payment_date', 'postmark_date')
    ordering = ('payment_date','account')
    readonly_fields = ['account', 'amount', 'instrument_number', 'memo', 'type_code', 'payment_date', 'postmark_date', 'processed_date']
    search_fields = ['account__account_number', 'instrument_number', 'amount', 'memo']

admin.site.register(PaymentHistory, PaymentHistoryAdmin)