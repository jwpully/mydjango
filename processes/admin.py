from django.contrib import admin
from models import Process, ProcessUser, StringParameter, DateParameter, StringParameterUser, DateParameterUser
from django.conf import settings
from cbase.views import isLoggedIn

# Register your models here.

class StringParameterInline(admin.TabularInline):
    fields = ['name', 'code', 'parameter', 'process']
    extra = 1
    model = StringParameter

class DateParameterInline(admin.TabularInline):
    fields = ['name', 'code', 'parameter', 'process']
    extra = 1
    model = DateParameter

class ProcessAdmin(admin.ModelAdmin):
    fields = ['name', 'code', 'description', 'path', 'group', 'run']
    list_display = ('name', 'run', 'run_process')
    ordering = ('name',)
    inlines = [DateParameterInline, StringParameterInline]

    def run_process(self, obj):
        return str('<a target="_blank" href="' + str(settings.CUSTOM_PATH) + str(obj.path) + '">Run Now</a>')
    run_process.allow_tags = True
    run_process.short_description = 'Run Process'

admin.site.register(Process, ProcessAdmin)

class StringParameterUserInline(admin.TabularInline):
    fields = ['name', 'code', 'parameter', 'process']
    extra = 0
    readonly_fields = ['name', 'code']
    model = StringParameterUser

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

class DateParameterUserInline(admin.TabularInline):
    fields = ['name', 'code', 'parameter', 'process']
    extra = 0
    readonly_fields = ['name', 'code']
    model = DateParameterUser

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

class ProcessUserAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'run']
    list_display = ('name', 'run', 'run_process')
    ordering = ('name',)
    readonly_fields = ['name', 'description']
    inlines = [DateParameterUserInline, StringParameterUserInline]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def run_process(self, obj):
        return str('<a target="_blank" href="' + str(settings.CUSTOM_PATH) + str(obj.path) + '">Run Now</a>')
    run_process.allow_tags = True
    run_process.short_description = 'Run Process'

    def get_queryset(self, request):
        qs = super(ProcessUserAdmin, self).get_queryset(request)
        loggedIn = isLoggedIn(request)
        return qs.filter(group__in=loggedIn[1])

admin.site.register(ProcessUser, ProcessUserAdmin)

