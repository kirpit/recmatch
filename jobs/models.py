from django.db import models
from common.choices import WORK_TYPE, STATUS, TERMS
from employers.models import Employer
from industries.models import JobClassification
from specs.models import WorkType, Location, Skill


class Job(models.Model):
    JobID = models.AutoField(primary_key=True)
    Status = models.CharField(max_length=16, choices=STATUS, default='open')
    JobTitle = models.CharField(max_length=32)
    ContractTerm = models.CharField(max_length=16, choices=WORK_TYPE)
    ContractDuration = models.PositiveSmallIntegerField(help_text='How many months?')
    NoOfVacancy = models.PositiveSmallIntegerField(default=1)
    Description = models.TextField(blank=True)
    PostingDate = models.DateField(auto_now_add=True)
    SalaryTerm = models.CharField(max_length=16, blank=True, choices=TERMS)
    SalaryMin = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    SalaryMax = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ContactPerson = models.CharField(max_length=32, blank=True)
    EmployerID = models.ForeignKey(Employer)
    WorkTypeID = models.ForeignKey(WorkType)
    LocationID = models.ForeignKey(Location)
    Industries = models.ManyToManyField(JobClassification, through='SubClassification')
    Skills = models.ManyToManyField(Skill, through='JobSkillSpec')

    def __unicode__(self):
        return self.JobTitle


class SubClassification(models.Model):
    RoleID = models.AutoField(primary_key=True)
    IndustryID = models.ForeignKey(JobClassification)
    JobID = models.ForeignKey(Job)
    pass


class JobSkillSpec(models.Model):
    JobID = models.ForeignKey(Job)
    SkillID = models.ForeignKey(Skill)
    Level = models.PositiveSmallIntegerField()
    YearOfExperience = models.PositiveSmallIntegerField()
    pass