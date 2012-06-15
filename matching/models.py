from django.db import models
from jobs.models import Job
from jobseekers.models import JobSeeker


class ShortList(models.Model):
    ShortListID = models.AutoField(primary_key=True)
    JobID = models.ForeignKey(Job)
    GenerateDate = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.JobID)


class Ranking(models.Model):
    RankID = models.AutoField(primary_key=True)
    ShortListID = models.ForeignKey(ShortList)
    JobSeekerID = models.ForeignKey(JobSeeker)
    GenerateDate = models.DateField(auto_now_add=True)
    Rank = models.PositiveSmallIntegerField(blank=True, null=True)

    def __unicode__(self):
        return '%s - %s' % (self.ShortListID, self.JobSeekerID)


class Interview(models.Model):
    InterviewID = models.AutoField(primary_key=True)
    RankID = models.ForeignKey(Ranking)
    DateTime = models.DateField()
    Result = models.CharField(max_length=254, blank=True, null=True)
    pass