from django.db import models

# Create your models here.
class GuestAppointmwntDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(max_length=15, null=True, blank=True)
    Department = models.CharField(max_length=100, null=True, blank=True)
    Date = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=10000, null=True, blank=True)
    Fee = models.IntegerField(null=True, blank=True)