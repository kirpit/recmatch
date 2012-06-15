from django.db import models
from employers.models import Employer
from jobs.models import Job

class Staff(models.Model):
    StaffID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=32)
    LastName = models.CharField(max_length=32)
    Position = models.CharField(max_length=32, blank=True)
    Phone = models.CharField(max_length=32, blank=True)
    Email = models.EmailField(blank=True)
    StartDate = models.DateField()
    FinishDate = models.DateField(blank=True, null=True)
    Employers = models.ManyToManyField(Employer, through='ContactStaff')
    Jobs = models.ManyToManyField(Job, through='Handler')

    @property
    def FullName(self):
        return '%s %s' % (self.FirstName, self.LastName)

    def __unicode__(self):
        return '%s %s' % (self.FirstName, self.LastName)


class ContactStaff(models.Model):
    StaffID = models.ForeignKey(Staff)
    EmployerID = models.ForeignKey(Employer)


class Handler(models.Model):
    StaffID = models.ForeignKey(Staff)
    JobID = models.ForeignKey(Job)

