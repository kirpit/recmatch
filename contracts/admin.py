from django.contrib import admin
from contracts.models import Contract, Contractor


class ContractorAdmin(admin.ModelAdmin):
    list_display = (
        'JobSeekerID',
        'ABN',
        'TFN',
        'AccountNo',
        'StartDate',
    )
    list_display_links = list_display

class ContractAdmin(admin.ModelAdmin):
    list_display = (
        'ContractID',
        'ContractorID',
        'JobID',
        'ContractDate',
        'Type',
        'PaymentTerm',
    )
    list_display_links = list_display


admin.site.register(Contractor, ContractorAdmin)
admin.site.register(Contract, ContractAdmin)
