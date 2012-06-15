from django.contrib import admin
from staffs.models import Staff


class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'StaffID',
        'FullName',
        'Position',
        'Phone',
        'Email',
        'StartDate',
    )
    list_display_links = list_display

admin.site.register(Staff, StaffAdmin)