# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *

# Register your models here.
admin.site.register(RegistrationModel)
admin.site.register(ContactDetailsModel)
admin.site.register(ContractorModel)

admin.site.register(PhoneNumber)

admin.site.register(Email)
admin.site.register(Website)
admin.site.register(PrincipalOwner)
admin.site.register(RegisteredOffice)
admin.site.register(DirectorDetails)
admin.site.register(WorkPerformanceDetails)
admin.site.register(ContactPersonDetails)
admin.site.register(CertificateIncorporation)
admin.site.register(CompanyProfileFile)
admin.site.register(OrganizationChart)
admin.site.register(PastProjects)
admin.site.register(FormCO2)
admin.site.register(FormCO7)
admin.site.register(FormCO10)
admin.site.register(DPRCertificate)
admin.site.register(AuditAccount)
admin.site.register(VATCertificate)
admin.site.register(CompanyTax)
admin.site.register(WCIC)
admin.site.register(CompanyProfile)
admin.site.register(QMS)
admin.site.register(CountryCodeMaster)



