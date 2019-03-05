# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
import json
from models import GeneralPurpose, MajorCategory, WaterBoreHole


class ContractServiceSubmit(View):
    def post(self,request):

        general_purpose = GeneralPurpose.objects.create(user=request.user)
        if request.POST.get('works'):
            for i in request.POST.getlist('works'):
                general_purpose.works.add(i)
        if request.POST.get('maintenence'):
            for i in request.POST.getlist('maintenence'):
                general_purpose.maintenence.add(i)
        if request.POST.get('supply'):
            for i in request.POST.getlist('supply'):
                general_purpose.supply.add(i)

        major_cat = MajorCategory.objects.create(user=request.user)
        if request.POST.get('rehabcivil'):
            for i in request.POST.getlist('rehabcivil'):
                major_cat.rehabcivil.add(i)
        if request.POST.get('rehabmech'):
            for i in request.POST.getlist('rehabmech'):
                major_cat.rehabmech.add(i)
        if request.POST.get('rehabelectr'):
            for i in request.POST.getlist('rehabelectr'):
                major_cat.rehabelectr.add(i)
        if request.POST.get('general_suppl'):
            for i in request.POST.getlist('general_suppl'):
                major_cat.general_suppl.add(i)
        if request.POST.get('heat_prods'):
            for i in request.POST.getlist('heat_prods'):
                major_cat.heat_prods.add(i)
        if request.POST.get('safety_lab_prods'):
            for i in request.POST.getlist('safety_lab_prods'):
                major_cat.safety_lab_prods.add(i)
        if request.POST.get('mech_parts'):
            for i in request.POST.getlist('mech_parts'):
                major_cat.mech_parts.add(i)
        if request.POST.get('consultancy'):
            for i in request.POST.getlist('consultancy'):
                major_cat.consultancy.add(i)
        if request.POST.get('waterborehole'):
            major_cat.waterborehole = WaterBoreHole.objects.get(id=request.POST.get('waterborehole'))
            major_cat.save()
        if request.POST.get('protologi'):
            for i in request.POST.getlist('protologi'):
                major_cat.protologi.add(i)
        if request.POST.get('lab'):
            for i in request.POST.getlist('lab'):
                major_cat.lab.add(i)
        if request.POST.get('onshore'):
            for i in request.POST.getlist('onshore'):
                major_cat.onshore.add(i)

        return HttpResponse(json.dumps('success'), content_type='json')
