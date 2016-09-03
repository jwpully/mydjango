from django.contrib import admin
from models import Export, ExportUser, StringParameter, StringParameterUser, DateParameter, DateParameterUser
from django.conf import settings
from cbase.views import isLoggedIn

# Register your models here.

class StringParameterInline(admin.TabularInline):
    fields = ['name', 'code', 'parameter', 'export']
    extra = 1
    model = StringParameter

class DateParameterInline(admin.TabularInline):
    fields = ['name', 'code', 'parameter', 'export']
    extra = 1
    model = DateParameter

class ExportAdmin(admin.ModelAdmin):
    fields = ['name', 'code', 'description', 'path', 'group', 'run']
    list_display = ('name', 'run', 'run_export')
    ordering = ('name',)
    inlines = [DateParameterInline, StringParameterInline]

    def run_export(self, obj):
        return str('<a target="_self" href="' + str(settings.CUSTOM_PATH) + str(obj.path) + '">Run Now</a>')
    run_export.allow_tags = True
    run_export.short_description = 'Run Export'

admin.site.register(Export, ExportAdmin)

class StringParameterUserInline(admin.TabularInline):
    fields = ['name', 'code', 'parameter', 'export']
    extra = 0
    readonly_fields = ['name', 'code']
    model = StringParameterUser

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

class DateParameterUserInline(admin.TabularInline):
    fields = ['name', 'code', 'parameter', 'export']
    extra = 0
    readonly_fields = ['name', 'code']
    model = DateParameterUser

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

class ExportUserAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'run']
    list_display = ('name', 'run', 'run_export')
    ordering = ('name',)
    readonly_fields = ['name', 'description']
    inlines = [DateParameterUserInline, StringParameterUserInline]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def run_export(self, obj):
        return str('<a target="_self" href="' + str(settings.CUSTOM_PATH) + str(obj.path) + '">Run Now</a>')
    run_export.allow_tags = True
    run_export.short_description = 'Run Export'

    def get_queryset(self, request):
        qs = super(ExportUserAdmin, self).get_queryset(request)
        loggedIn = isLoggedIn(request)
        return qs.filter(group__in=loggedIn[1])

admin.site.register(ExportUser, ExportUserAdmin)
