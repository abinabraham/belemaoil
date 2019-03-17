# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *



admin.site.register(Maintenence)
admin.site.register(Works)

admin.site.register(Supply)

admin.site.register(GeneralPurpose)

models = [RehabCivil, RehabMech ,RehabElectr ,GeneralSupplies ,HeatingCoolingProd, SafetyLabChem, MechanicalParts, \
Consultancy, WaterBoreHole, ProtocolLogistics, Laboratory ,OnshoreEnv, MajorCategory, InstllMaintModel, \
		  Survey, AviationSupport, IntegrityTest, Calibration, Haulage, MediPharma, Hospitality,Printing,Automob, DataMeasur, \
		  OffshorPipe, OnshorPipe, FacilityMaint, InstallationUpgrade, DisciplineEng]

for model in models:
	admin.site.register(model)
