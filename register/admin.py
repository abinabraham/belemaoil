# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import RegistrationModel,ContactDetailsModel,ContractorModel,PhoneNumber,Email,Website


# Register your models here.
admin.site.register(RegistrationModel)
admin.site.register(ContactDetailsModel)
admin.site.register(ContractorModel)

admin.site.register(PhoneNumber)

admin.site.register(Email)
admin.site.register(Website)

