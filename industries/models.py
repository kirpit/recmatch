from django.db import models


class JobClassification(models.Model):
    IndustryID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.Name


