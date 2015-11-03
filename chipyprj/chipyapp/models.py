
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

class VideoPen(models.Model):
    time = models.IntegerField()
    pen = models.FloatField()
    complex_code = models.ForeignKey('Complex')

class HSDPen(models.Model):
    time = models.IntegerField()
    pen = models.FloatField()
    complex_code = models.ForeignKey('Complex')

class CDVPen(models.Model):
    time = models.IntegerField()
    pen = models.FloatField()
    complex_code = models.ForeignKey('Complex')

class XHSPen(models.Model):
    time = models.IntegerField()
    pen = models.FloatField()
    complex_code = models.ForeignKey('Complex')

class VideoActive(models.Model):
    time = models.IntegerField()
    active = models.IntegerField()
    complex_code = models.ForeignKey('Complex')

class HSDActive(models.Model):
    time = models.IntegerField()
    active = models.IntegerField()
    complex_code = models.ForeignKey('Complex')

class CDVActive(models.Model):
    time = models.IntegerField()
    active = models.IntegerField()
    complex_code = models.ForeignKey('Complex')

class XHSActive(models.Model):
    time = models.IntegerField()
    active = models.IntegerField()
    complex_code = models.ForeignKey('Complex')

