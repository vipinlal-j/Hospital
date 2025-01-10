from django.db import models

# Create your models here.
class DepartmentDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(max_length=15, null=True, blank=True)
    HOD = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=10000, null=True, blank=True)
class StaffDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Type = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(max_length=15, null=True, blank=True)
    Qualifications = models.CharField(max_length=100, null=True, blank=True)
    Department = models.CharField(max_length=100, null=True, blank=True)
    DOB = models.CharField(max_length=100, null=True, blank=True)

