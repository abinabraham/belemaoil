# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import FormView,TemplateView, View
from django.contrib.auth.models import User
from register.forms import LoginForm
from register.models import ContractorModel
from services.models import MajorCategory
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class LoginView(FormView, View):

    template_name = 'dashboard/login.html'
    form_class = LoginForm
    success_url = reverse_lazy("dashboard_home")

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'  
    login_url = '/dashboard/login/'  

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        ctx['contracts_count'] = ContractorModel.objects.count()
        ctx['services_count'] = MajorCategory.objects.count()
        ctx['user_count'] = User.objects.count()    
        return ctx

class LogoutView(LoginRequiredMixin, View):
    template_name = 'dashboard/cinfo.html'
    login_url = '/dashboard/login/'  

    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('dashboard_login')

class CInfoView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/cinfo.html'
    login_url = '/dashboard/login/'  

    def get_context_data(self, **kwargs):
        ctx = super(CInfoView, self).get_context_data(**kwargs)
        contract_list = ContractorModel.objects.all()
        page = self.request.GET.get('page', 1)
        paginator = Paginator(contract_list, 10)
        try:
            contract_list = paginator.page(page)
        except PageNotAnInteger:
            contract_list = paginator.page(1)
        except EmptyPage:
            contract_list = paginator.page(paginator.num_pages)


        ctx['contracts'] = contract_list
        return ctx



