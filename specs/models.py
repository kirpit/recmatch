from django.db import models
from common.choices import WORK_TYPE


class WorkType(models.Model):
    WorkTypeID = models.AutoField(primary_key=True)
    Type = models.CharField(max_length=16, choices=WORK_TYPE, unique=True)

    def __unicode__(self):
        return self.get_Type_display()


class Location(models.Model):
    LocationID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.Name


class Skill(models.Model):
    SkillID = models.AutoField(primary_key=True)
    SkillName = models.CharField(max_length=32)
    Type = models.CharField(max_length=32, blank=True, null=True)

    def __unicode__(self):
        return self.SkillName