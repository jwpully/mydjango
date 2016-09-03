from django.contrib import admin
from models import Property
from alterations.models import Alteration
# Register your models here.

class AlterationsInline(admin.StackedInline):
    fields = [('property', 'account', 'status', 'email'), ('fence', 'shed', 'pool', 'room', 'driveway', 'garage', 'deck', 'other') \
        , ('structureother')
        , ('builder', 'buildername'), ('size', 'roof', 'cost', 'completion')
        , ('description')
        , ('file1', 'file2', 'file3')
        , ('requested', 'finalized', 'processed'), ('notes'), ('waiver'), ('reason', 'special_instructions')]
    readonly_fields = ['processed', 'requested']
    extra = 0
    model = Alteration

class PropertiesAdmin(admin.ModelAdmin):
    fields = ['number', 'street', 'section' ,'lot']
    list_display = ('number', 'street', 'section', 'lot')
    ordering = ('number', 'street', 'section', 'lot')
    readonly_fields = ['number', 'street', 'section', 'lot']
    search_fields = ['number', 'street']
    inlines = [AlterationsInline]

admin.site.register(Property, PropertiesAdmin)
