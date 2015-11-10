
from django.db import models

class Module(models.Model):
    module_number = models.IntegerField()
    def __unicode__(self):
       return unicode(self.module_number)

class Area(models.Model):
    area = models.CharField(max_length=10)
    def __unicode__(self):
       return unicode(self.area)

class Complex(models.Model):
    complex_name = models.CharField(max_length=500, blank=True)
    complex_code = models.CharField(max_length=10)
    hmc = models.CharField(max_length=4, blank=True)
    unit = models.IntegerField()
    module = models.ForeignKey('Module')
    area = models.ForeignKey('Area')

class DataType(models.Model):
    name = models.CharField(max_length=10)

class Penetration(models.Model):
    year = models.SmallIntegerField()
    quarter = models.SmallIntegerField()
    penetration = models.FloatField()
    complex_code = models.ForeignKey('Complex')
    data_type = models.ForeignKey('DataType')

class ActiveUnit(models.Model):
    year = models.SmallIntegerField()
    quarter = models.SmallIntegerField()
    time = models.IntegerField()
    active_unit = models.IntegerField()
    complex_code = models.ForeignKey('Complex')
    data_type = models.ForeignKey('DataType')

