from django.contrib import admin
from models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'code', 'description', 'price', 'active_flag']
    list_display = ('name', 'description', 'price', 'active_flag')
    ordering = ('-active_flag', 'name',)

admin.site.register(Product, ProductAdmin)
