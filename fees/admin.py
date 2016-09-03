from django.contrib import admin
from models import Fee
# Register your models here.

class FeeAdmin(admin.ModelAdmin):
    fields = ['name', 'code', 'description', 'value', 'fee_type', 'active_flag']
    list_display = ('name', 'description', 'value', 'fee_type', 'active_flag')
    ordering = ('name',)

admin.site.register(Fee, FeeAdmin)

