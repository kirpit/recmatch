from django.contrib import admin
from timesheets.models import TimeSheet, Payment


class TimeSheetAdmin(admin.ModelAdmin):
    list_display = (
        'TimeSheetID',
        'ContractID',
        'StartDate',
        'FinishDate',
    )
    list_display_links = list_display


class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'PaymentID',
        'TimeSheetID',
        'PaymentTerm',
        'AmountToPay',
        'AmountPaid',
        'DatePaid',
    )
    list_display_links = list_display


admin.site.register(TimeSheet, TimeSheetAdmin)
admin.site.register(Payment, PaymentAdmin)