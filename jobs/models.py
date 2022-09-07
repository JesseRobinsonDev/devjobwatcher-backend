from django.db import models
from django_mysql.models import ListCharField

class Job(models.Model):
    jobTitle = models.CharField(max_length=64, blank=False, default='')
    jobBody = models.TextField(blank=False, default='')
    jobCompany = models.CharField(max_length=64, blank=False, default='')
    jobType = ListCharField(base_field=models.CharField(max_length=16), null=True, max_length=(10*10))
    jobLevel = models.CharField(max_length=64, null=True)
    jobIndustry = ListCharField(base_field=models.CharField(max_length=16), null=True, max_length=(10*10))
    jobSalaryLow = models.IntegerField(null=True)
    jobSalaryHigh = models.IntegerField(null=True)
    jobSalaryFrequency = models.CharField(max_length=64, null=True)
    jobRemote = models.BooleanField(blank=False, default=False)
    jobTechnologies = ListCharField(base_field=models.CharField(max_length=16), null=True, max_length=(10*10))
    jobLink = models.TextField(blank=False, default='')
    jobSiteID = models.CharField(max_length=64, blank=False, default='', unique=True)