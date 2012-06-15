from django.db import models
from industries.models import JobClassification
from staffs.models import Staff
from common.choices import STATUS, TERMS
from specs.models import Location, WorkType, Skill

# Create your models here.

class JobSeeker(models.Model):
    JobSeekerID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=32)
    LastName = models.CharField(max_length=32)
    DateOfBirth = models.DateField(blank=True, null=True)
    Phone = models.CharField(max_length=32, blank=True)
    Address = models.TextField(blank=True)
    City = models.CharField(max_length=32, blank=True)
    Country = models.CharField(max_length=32, blank=True)
    Postcode = models.CharField(max_length=4, blank=True)
    Email = models.EmailField()
    Status = models.CharField(max_length=16, choices=STATUS, default='open')
    StaffID = models.OneToOneField(Staff)
    Locations = models.ManyToManyField(Location, through='JobSeekerLocation')
    WorkTypes = models.ManyToManyField(WorkType, through='JobSeekerWorkType')
    Industries = models.ManyToManyField(JobClassification, through='JobSeekerRole')
    Skills = models.ManyToManyField(Skill, through='JobSeekerSkill')

    @property
    def FullName(self):
        return '%s %s' % (self.FirstName, self.LastName)

    def __unicode__(self):
        return '%s %s' % (self.FirstName, self.LastName)


class JobSeekerLocation(models.Model):
    JobSeekerID = models.ForeignKey('JobSeeker')
    LocationID = models.ForeignKey(Location)
    Preference = models.PositiveSmallIntegerField(default=1)


class JobSeekerWorkType(models.Model):
    JobSeekerID = models.ForeignKey('JobSeeker')
    WorkTypeID = models.ForeignKey(WorkType)
    Preference = models.PositiveSmallIntegerField(default=1)
    SalaryTerm = models.CharField(max_length=16, choices=TERMS, blank=True)
    MinSalary = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)


class Resume(models.Model):
    ResumeID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=32)
    Filepath = models.FileField(upload_to='resumes/')
    JobSeekerID = models.ForeignKey(JobSeeker)

    def JobSeekerFullName(self):
        return self.JobSeekerID.FullName


class JobSeekerRole(models.Model):
    RoleID = models.AutoField(primary_key=True)
    JobSeekerID = models.ForeignKey(JobSeeker)
    IndustryID = models.ForeignKey(JobClassification)
    Preference = models.PositiveSmallIntegerField(default=1)
    pass


class JobSeekerSkill(models.Model):
    JobSeekerID = models.ForeignKey(JobSeeker)
    SkillID = models.ForeignKey(Skill)
    Level = models.PositiveSmallIntegerField()
    YearOfExperience = models.PositiveSmallIntegerField()
    pass
