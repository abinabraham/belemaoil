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
  class Meta:
    ordering = ['name']

class RehabMech(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name
  class Meta:
    ordering = ['name']

class RehabElectr(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name
  class Meta:
    ordering = ['name']

class GeneralSupplies(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name
  class Meta:
    ordering = ['name']

class HeatingCoolingProd(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name
  class Meta:
    ordering = ['name']

class SafetyLabChem(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name
  class Meta:
    ordering = ['name']


class MechanicalParts(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name
  class Meta:
    ordering = ['name']

class Consultancy(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name
  class Meta:
    ordering = ['name']

class WaterBoreHole(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name
  class Meta:
    ordering = ['name']

class ProtocolLogistics(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name
  class Meta:
    ordering = ['name']

class Laboratory(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name
  class Meta:
    ordering = ['name']

class OnshoreEnv(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name
  class Meta:
    ordering = ['name']


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

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.user.first_name