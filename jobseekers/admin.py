from django.contrib import admin
from jobseekers.models import JobSeeker, Resume

class JobSeekerAdmin(admin.ModelAdmin):
    list_display = (
        'JobSeekerID',
        'FullName',
        'Status',
        'Phone',
        'Email',
        'City',
        'Country',
    )
    list_display_links = ('JobSeekerID', 'FullName', )


class ResumeAdmin(admin.ModelAdmin):
    list_display = (
        'ResumeID',
        'Title',
        'JobSeekerFullName',
    )
    list_display_links = list_display



admin.site.register(JobSeeker, JobSeekerAdmin)
admin.site.register(Resume, ResumeAdmin)