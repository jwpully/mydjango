from django.contrib import admin
from models import CustomerView, PaymentView
from django.conf import settings
# Register your models here.

class PaymentsInline(admin.TabularInline):
    fields = ['payment_date', 'amount', 'postmark_date', 'processed_date', 'customer']
    readonly_fields = ['payment_date', 'amount', 'postmark_date', 'processed_date', 'customer']
    extra = 0
    model = PaymentView

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

class CustomerViewAdmin(admin.ModelAdmin):
    fields = ['contact_name', 'contact_address', 'account', 'total_charges', 'balance']
    list_display = ('contact_name', 'account', 'balance', 'view_statement')
    ordering = ('account',)
    readonly_fields = ['contact_name', 'contact_address', 'account', 'total_charges', 'balance']
    search_fields = ['contact_name', 'contact_address', 'account__account_number']
    inlines = [PaymentsInline]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def view_statement(self, obj):
        return str('<a target="_blank" href="'+ str(settings.CUSTOM_PATH) + 'statements/single/' + str(obj.id) + '">View Statement</a>')
    view_statement.allow_tags = True
    view_statement.short_description = 'Statement'


admin.site.register(CustomerView, CustomerViewAdmin)

