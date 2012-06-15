from django.contrib import admin
from employers.models import Employer

class EmployerAdmin(admin.ModelAdmin):
    list_display = (
        'EmployerID',
        'Name',
        'Phone',
        'Email',
        'City',
        'Country',
    )
    list_display_links = ('EmployerID', 'Name', )


admin.site.register(Employer, EmployerAdmin)