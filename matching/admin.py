from django.contrib import admin
from matching.models import ShortList, Ranking, Interview

class ShortListAdmin(admin.ModelAdmin):
    list_display = (
        'ShortListID',
        'JobID',
        'GenerateDate',
        'Employer',
    )
    list_display_links = list_display

    def Employer(self, obj):
        return obj.JobID.EmployerID


class RankingAdmin(admin.ModelAdmin):
    list_display = (
        'RankID',
        'ShortListID',
        'JobSeekerID',
        'GenerateDate',
        'Rank',
    )
    list_display_links = list_display


class InterviewAdmin(admin.ModelAdmin):
    list_display = (
        'InterviewID',
        'RankID',
        'DateTime',
        'Result',
    )
    list_display_links = list_display


admin.site.register(ShortList, ShortListAdmin)
admin.site.register(Ranking, RankingAdmin)
admin.site.register(Interview, InterviewAdmin)