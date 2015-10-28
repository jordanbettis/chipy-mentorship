from django.db import models

class Module(models.Model):
    module_number = models.IntegerField()

class Area(models.Model):
    area = models.CharField(max_length=10)

class Complex(models.Model):
    complex_name = models.CharField(max_length=500, blank=True)
    complex_code = models.CharField(max_length=6)
    hmc = models.CharField(max_length=4, blank=True)
    module = models.ForeignKey('Module')
    area = models.ForeignKey('Area')

