from django.contrib import admin
from models import Member
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    fields = [('first_name', 'last_name'), 'position', ('start_term', 'end_term'), ('start_role', 'end_role'), ('active_flag'), ('duty')]
    list_display = ['first_name', 'last_name', 'position', 'start_term' ,'end_term']
    ordering = ('last_name', 'first_name')

admin.site.register(Member, MemberAdmin)
