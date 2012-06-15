from django.db import models
from common.choices import TERMS
from contracts.models import Contract

class TimeSheet(models.Model):
    TimeSheetID = models.AutoField(primary_key=True)
    ContractID = models.ForeignKey(Contract)
    WorkHours = models.PositiveSmallIntegerField()
    StartDate = models.DateField()
    FinishDate = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return '%s %s/%s' % (self.ContractID, self.StartDate, self.FinishDate)


class Payment(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    TimeSheetID = models.ForeignKey(TimeSheet)
    PaymentTerm = models.CharField(max_length=16, choices=TERMS)
    AmountToPay = models.DecimalField(max_digits=12, decimal_places=2)
    AmountPaid = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    DatePaid = models.DateField(blank=True, null=True)
    GrossIncome = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    NetIncome = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    IncomeTax = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    Super = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    GrossCommission = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    pass


