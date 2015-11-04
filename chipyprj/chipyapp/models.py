
from django.db import models

class Module(models.Model):
    module_number = models.IntegerField()

class Area(models.Model):
    area = models.CharField(max_length=10)

class Complex(models.Model):
    complex_name = models.CharField(max_length=500, blank=True)
    complex_code = models.CharField(max_length=6)
    hmc = models.CharField(max_length=4, blank=True)
    unit = models.IntegerField()
    module = models.ForeignKey('Module')
    area = models.ForeignKey('Area')

class DataType(models.Model):
    video = models.CharField(max_length=10)
    hsd = models.CharField(max_length=10)
    cdv = models.CharField(max_length=10)
    xhs = models.CharField(max_length=10)

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

