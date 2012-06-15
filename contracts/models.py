from django.db import models
from common.choices import WORK_TYPE, TERMS
from jobseekers.models import JobSeeker
from jobs.models import Job

class Contractor(models.Model):
    ContractorID = models.AutoField(primary_key=True)
    JobSeekerID = models.ForeignKey(JobSeeker, unique=True)
    AccountType = models.CharField(max_length=16, choices=WORK_TYPE)
    ABN = models.CharField(max_length=16, blank=True)
    TFN = models.CharField(max_length=16, blank=True)
    AccountNo = models.CharField(max_length=16, blank=True, null=True)
    StartDate = models.DateField()

    def __unicode__(self):
        return '%s %s' % (self.JobSeekerID.FirstName, self.JobSeekerID.LastName)


class Contract(models.Model):
    ContractID = models.AutoField(primary_key=True)
    ContractorID = models.ForeignKey(Contractor)
    JobID = models.ForeignKey(Job)
    ContractDate = models.DateField()
    Type = models.CharField(max_length=16, choices=WORK_TYPE)
    PaymentTerm = models.CharField(max_length=16, choices=TERMS)
    PayGrade = models.PositiveIntegerField(blank=True, null=True)
    StartDate = models.DateField()
    EndDate = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return '%s / %s' % (self.ContractorID, self.JobID)


