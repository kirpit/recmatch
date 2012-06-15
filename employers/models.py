from django.db import models

class Employer(models.Model):
    EmployerID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=32)
    ABN = models.CharField(max_length=16, blank=True)
    Phone = models.CharField(max_length=16, blank=True)
    Email = models.EmailField(blank=True)
    Address = models.TextField(blank=True)
    Postcode = models.CharField(max_length=4, blank=True)
    City = models.CharField(max_length=16, blank=True)
    Country = models.CharField(max_length=32, blank=True)

    def __unicode__(self):
        return self.Name