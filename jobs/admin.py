from django.contrib import admin
from jobs.models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = (
        'JobID',
        'Status',
        'JobTitle',
        'NoOfVacancy',
        'EmployerID',
        'ContractTerm',
        'ContactPerson',
    )
    list_display_links = list_display


admin.site.register(Job, JobAdmin)