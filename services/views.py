# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
import json


class ContractServiceSubmit(View):
    def post(self,request):
        print "sssssssssssss",request.POST
        return HttpResponse(json.dumps('success'), content_type='json')
