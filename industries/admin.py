from django.contrib import admin
from industries.models import JobClassification

#class JobClassificationAdmin(admin.ModelAdmin):
#    list_display = ('JobSeekerID', 'FullName', )
#    list_display_links = ('FullName', )
#
#    def FullName(self, obj):
#        return '%s %s' % (obj.FirstName, obj.LastName)
#
#    FullName.short_description = 'Full Name'


admin.site.register(JobClassification)