
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

    def __unicode__(self):
       return "{} {}".format(self.complex_name, self.complex_code)

class LOB(models.Model):
    lob = models.CharField(max_length=10)
    def __unicode__(self):
       return unicode(self.lob)

class Penetration(models.Model):
    year = models.SmallIntegerField()
    quarter = models.SmallIntegerField()
    penetration = models.FloatField()
    complex_code = models.ForeignKey('Complex')
    lob = models.ForeignKey('LOB')
    def __unicode__(self):
       return unicode(self.penetration)

class ActiveUnit(models.Model):
    year = models.SmallIntegerField()
    quarter = models.SmallIntegerField()
    active_unit = models.IntegerField()
    complex_code = models.ForeignKey('Complex')
    lob = models.ForeignKey('LOB')

    def __unicode__(self):
       return unicode(self.active_unit)

