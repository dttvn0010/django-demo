from django.db import models

class Location(models.Model):
    line1 = models.CharField(max_length=200, verbose_name='Address Line 1')
    line2 = models.CharField(max_length=200, verbose_name='Address Line 2')
    postCode = models.CharField(max_length=200, verbose_name='Postcode')
    googleLocation = models.CharField(max_length=100, verbose_name='Google Location')

    def __str__(self):
        return f"{self.line1}, {self.line2}"

class Device(models.Model):
    unitID1 = models.CharField(max_length=30, verbose_name="Unit ID #1")
    unitID2 = models.CharField(max_length=30, verbose_name="Unit ID #2")
    location = models.ForeignKey(Location, verbose_name='Installation  Location', on_delete=models.PROTECT)
    locationDescription = models.CharField(max_length=500, verbose_name="Description of Location")


