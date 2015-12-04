
from django.db import models

class Module(models.Model):
    module_number = models.IntegerField()
    def __unicode__(self):
       return unicode(self.module_number)

class Area(models.Model):
    area = models.CharField(max_length=10)
    def __unicode__(self):
       return unicode(self.area)

class ServiceStatus(models.Model):
    service_status = models.CharField(max_length=10)
    def __unicode__(self):
       return unicode(self.service_status)

class PropertyType(models.Model):
    property_type = models.CharField(max_length=20)
    def __unicode__(self):
       return unicode(self.property_type)

class Team(models.Model):
    team = models.CharField(max_length=10)
    def __unicode__(self):
       return unicode(self.team)

class Complex(models.Model):
    #complex_name = models.CharField(max_length=500, blank=True)
    complex_code = models.CharField(max_length=10)
    #hmc = models.CharField(max_length=4, blank=True)
    unit = models.IntegerField()
    module = models.ForeignKey('Module')
    area = models.ForeignKey('Area')
    service_status = models.ForeignKey('ServiceStatus', null=True, blank=True)
    property_type = models.ForeignKey('PropertyType',null=True, blank=True)
    team = models.ForeignKey('Team',null=True, blank=True)
    def __unicode__(self):
       return "{}".format(self.complex_code)

class LOB(models.Model):
    lob = models.CharField(max_length=10)
    def __unicode__(self):
       return unicode(self.lob)

class Penetration(models.Model):
    year = models.SmallIntegerField(db_index=True)
    quarter = models.SmallIntegerField(db_index=True)
    penetration = models.FloatField()
    complex_code = models.ForeignKey('Complex')
    lob = models.ForeignKey('LOB')
    def __unicode__(self):
       return unicode(self.penetration)

class ActiveUnit(models.Model):
    year = models.SmallIntegerField(db_index=True)
    quarter = models.SmallIntegerField(db_index=True)
    active_unit = models.IntegerField()
    complex_code = models.ForeignKey('Complex')
    lob = models.ForeignKey('LOB')
    def __unicode__(self):
       return unicode(self.active_unit)

