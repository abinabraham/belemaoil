# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Service models here.

class Works(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name
  class Meta:
    ordering = ['name']

class Maintenence(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name
  class Meta:
    ordering = ['name']



class Supply(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name
  class Meta:
    ordering = ['name']



class GeneralPurpose(models.Model):

    user = models.ForeignKey(User)
    works = models.ManyToManyField(Works,null=True, blank= True)
    maintenence = models.ManyToManyField(Maintenence,null=True, blank= True)
    supply = models.ManyToManyField(Supply,null=True, blank= True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.user.first_name

class RehabCivil(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name


class RehabMech(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name


class RehabElectr(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name


class GeneralSupplies(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name


class HeatingCoolingProd(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name


class SafetyLabChem(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name



class MechanicalParts(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name


class Consultancy(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name


class WaterBoreHole(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name


class ProtocolLogistics(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name


class Laboratory(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name


class OnshoreEnv(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name


class InstllMaintModel(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name


class AviationSupport(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name

class Survey(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name



class IntegrityTest(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name


class Calibration(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name

class Haulage(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name

class MediPharma(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name



class Hospitality(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name

class Printing(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name


class Automob(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name


class DataMeasur(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name

class OffshorPipe(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name



class OnshorPipe(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name


class FacilityMaint(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name

class DisciplineEng(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name

class InstallationUpgrade(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name

class MajorCategory(models.Model):

    user = models.ForeignKey(User)
    rehabcivil = models.ManyToManyField(RehabCivil,null=True, blank= True)
    rehabmech = models.ManyToManyField(RehabMech,null=True, blank= True)
    rehabelectr = models.ManyToManyField(RehabElectr,null=True, blank= True)
    general_suppl = models.ManyToManyField(GeneralSupplies,null=True, blank= True)
    heat_prods = models.ManyToManyField(HeatingCoolingProd,null=True, blank= True)
    safety_lab_prods = models.ManyToManyField(SafetyLabChem,null=True, blank= True)
    mech_parts = models.ManyToManyField(MechanicalParts,null=True, blank= True)
    consultancy = models.ManyToManyField(Consultancy,null=True, blank= True)
    waterborehole = models.ForeignKey(WaterBoreHole,null=True, blank= True)
    protologi = models.ManyToManyField(ProtocolLogistics,null=True, blank= True)
    lab = models.ManyToManyField(Laboratory,null=True, blank= True)
    onshore = models.ManyToManyField(OnshoreEnv,null=True, blank= True)
    install = models.ManyToManyField(InstllMaintModel,null=True, blank= True)
    aviation = models.ManyToManyField(AviationSupport,null=True, blank= True)
    survey = models.ManyToManyField(Survey,null=True, blank= True)
    intetest = models.ManyToManyField(IntegrityTest,null=True, blank= True)
    calib = models.ManyToManyField(Calibration,null=True, blank= True)
    haul = models.ManyToManyField(Haulage,null=True, blank= True)
    medphr = models.ManyToManyField(MediPharma,null=True, blank= True)
    hosp = models.ManyToManyField(Hospitality,null=True, blank= True)
    printi = models.ManyToManyField(Printing,null=True, blank= True)
    automob = models.ManyToManyField(Automob,null=True, blank= True)
    datam = models.ManyToManyField(DataMeasur,null=True, blank= True)
    offshor = models.ManyToManyField(OffshorPipe,null=True, blank= True)
    onshor = models.ManyToManyField(OnshorPipe,null=True, blank= True)
    facil = models.ManyToManyField(FacilityMaint,null=True, blank= True)
    disc = models.ManyToManyField(DisciplineEng ,null=True, blank= True)
    installs = models.ManyToManyField( InstallationUpgrade,null=True, blank= True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.user.first_name