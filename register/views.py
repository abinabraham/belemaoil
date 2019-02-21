# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import FormView,TemplateView, View
from django.contrib.auth.models import User
from django.views.generic.edit import FormView

from register.forms import RegistrationForm,UserForm
from register.models import RegistrationModel
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from random import randint
import random
from django.views.generic import CreateView
import string
from forms import *
from django.conf import settings


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return str(''.join(random.choice(chars) for _ in range(size)))

class LandingPageView(FormView):
    form_class = ContractorModelForm
    template_name = 'landing.html'
    success_url = '/index/'


    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        phone_formset = PhoneNumberFormSet()
        email_formset = EmailFormSet()
        website_formset = WebsiteFormSet()
        reg_ofc_formset = RegisteredOfficeFormSet()
        principal_formset=PrincipalOwnerFormSet()
        dir_formset=DirectorDetailsFormSet()
        work_performance_formset = WorkPerformanceDetailsFormSet()
        contact_formset = ContactPersonDetailsFormSet()
        certfct_incorprtn = CertificateIncorporationFormSet()
        cmpny_profile_file = CompanyProfileFileFormSet()
        orgnztn_chart_formset=OrganizationChartFormSet()
        past_project_formset = PastProjectsFormSet()
        formco2_formset = FormCO2FormSet()
        formco7_formset = FormCO7FormSet()
        form_co10_formset = FormCO10FormSet()
        dpr_formset = DPRCertificateFormSet()
        audit_formset = AuditAccountFormSet()
        vat_formset = VATCertificateFormSet()
        tax_formset = CompanyTaxFormSet()
        wcic_formset = WCICFormSet()
        cmpny_profile_formset = CompanyProfileFormSet()
        QMS_formset = QMSFormSet()
        try:
            data_ob = RegistrationModel.objects.get(user=request.user)
        except:
            data_ob = None
        return self.render_to_response(
                  self.get_context_data(form=form,data_ob=data_ob,
                                        phone_formset=phone_formset,email_formset=email_formset,website_formset = website_formset, reg_ofc_formset=reg_ofc_formset,
                                        principal_formset=principal_formset,dir_formset=dir_formset,work_performance_formset=work_performance_formset,contact_formset=contact_formset,
                                        certfct_incorprtn=certfct_incorprtn,cmpny_profile_file=cmpny_profile_file,orgnztn_chart_formset=orgnztn_chart_formset,
                                        past_project_formset=past_project_formset,formco2_formset=formco2_formset,formco7_formset=formco7_formset,form_co10_formset=form_co10_formset,
                                        dpr_formset=dpr_formset,audit_formset=audit_formset,vat_formset=vat_formset,tax_formset=tax_formset,wcic_formset=wcic_formset,cmpny_profile_formset=cmpny_profile_formset,
                                        QMS_formset=QMS_formset)
                                     )

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
 
        phone_formset = PhoneNumberFormSet(self.request.POST)
        email_formset = EmailFormSet(self.request.POST)
        website_formset = WebsiteFormSet(self.request.POST)
        reg_ofc_formset = RegisteredOfficeFormSet(self.request.POST)
        principal_formset=PrincipalOwnerFormSet(self.request.POST)
        dir_formset = DirectorDetailsFormSet(self.request.POST)
        work_performance_formset = WorkPerformanceDetailsFormSet(self.request.POST,self.request.FILES)
        contact_formset = ContactPersonDetailsFormSet(self.request.POST)
        certfct_incorprtn = CertificateIncorporationFormSet(self.request.POST,self.request.FILES)
        cmpny_profile_file = CompanyProfileFileFormFormSet(self.request.POST,self.request.FILES)
        orgnztn_chart_formset=OrganizationChartFormSet(self.request.POST,self.request.FILES)
        past_project_formset = PastProjectsFormSet(self.request.POST,self.request.FILES)
        formco2_formset = FormCO2FormSet(self.request.POST,self.request.FILES)
        formco7_formset = FormCO7FormSet(self.request.POST,self.request.FILES)
        form_co10_formset = FormCO10FormSet(self.request.POST,self.request.FILES)
        dpr_formset = DPRCertificateFormSet(self.request.POST,self.request.FILES)
        audit_formset=AuditAccountFormSet(self.request.POST,self.request.FILES)

        vat_formset = VATCertificateFormSet(self.request.POST,self.request.FILES)
        tax_formset = CompanyTaxFormSet(self.request.POST,self.request.FILES)
        wcic_formset = WCICFormSet(self.request.POST,self.request.FILES)
        cmpny_profile_formset = CompanyProfileFormSet(self.request.POST,self.request.FILES)
        QMS_formset=QMS_formset(self.request.POST,self.request.FILES)
        
        if form.is_valid() and phone_formset.is_valid() and email_formset.is_valid() and \
        website_formset.is_valid() and reg_ofc_formset.is_valid() and principal_formset.is_valid() and dir_formset.is_valid() and \
        work_performance_formset.is_valid() and contact_formset.is_valid() and certfct_incorprtn.is_valid() and cmpny_profile_file.is_valid() and \
        orgnztn_chart_formset.is_valid() and past_project_formset.is_valid() and formco2_formset.is_valid() and formco7_formset.is_valid() and \
        form_co10_formset.is_valid() and dpr_formset.is_valid() and audit_formset.is_valid() and vat_formset.is_valid() and tax_formset.is_valid() and \
        wcic_formset.is_valid() and cmpny_profile_formset.is_valid() and QMS_formset.is_valid():
            return self.form_valid(form, phone_formset, email_formset, website_formset, reg_ofc_formset,principal_formset,dir_formset,work_performance_formset,contact_formset,certfct_incorprtn,cmpny_profile_file,orgnztn_chart_formset,past_project_formset,formco2_formset,formco7_formset,form_co10_formset,dpr_formset,audit_formset,vat_formset,tax_formset,wcic_formset,cmpny_profile_formset,QMS_formset)
        else:
            return self.form_invalid(form, phone_formset, email_formset, website_formset, reg_ofc_formset,principal_formset,dir_formset,work_performance_formset,contact_formset,certfct_incorprtn,cmpny_profile_file,orgnztn_chart_formset,past_project_formset,formco2_formset,formco7_formset,form_co10_formset,dpr_formset,audit_formset,vat_formset,tax_formset,wcic_formset,cmpny_profile_formset,QMS_formset)

    def form_valid(self, form, phone_formset, email_formset, website_formset, reg_ofc_formset,principal_formset,dir_formset,work_performance_formset,contact_formset,certfct_incorprtn,cmpny_profile_file,orgnztn_chart_formset,past_project_formset,formco2_formset,formco7_formset,form_co10_formset,dpr_formset,audit_formset,vat_formset,tax_formset,wcic_formset,cmpny_profile_formset,QMS_formset):
        """
        Called if all forms are valid. Creates Assignment instance along with the
        associated AssignmentQuestion instances then redirects to success url
        Args:
            form: Assignment Form
            assignment_question_form: Assignment Question Form

        Returns: an HttpResponse to success url

        """
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        # saving AssignmentQuestion Instances
        phone_formset = phone_formset.save(commit=False)
        for aq in phone_formset:
            aq.contract = self.object
            aq.save()
        email_formset = email_formset.save(commit=False)
        for aq in email_formset:
            aq.contract = self.object
            aq.save()
        website_formset = website_formset.save(commit=False)
        for aq in website_formset:
            aq.contract = self.object
            aq.save()
        reg_ofc_formset = reg_ofc_formset.save(commit=False)
        for aq in reg_ofc_formset:
            aq.contract = self.object
            aq.save()
        principal_formset = principal_formset.save(commit=False) 
        for aq in principal_formset:
            aq.contract = self.object
            aq.save()
        dir_formset = dir_formset.save(commit=False) 
        for aq in dir_formset:
            aq.contract = self.object
            aq.save()

        work_performance_formset = work_performance_formset.save(commit=False) 
        for aq in work_performance_formset:
            aq.contract = self.object
            aq.save()
        contact_formset=contact_formset.save(commit=False) 
        for aq in contact_formset:
            aq.contract = self.object
            aq.save()
        certfct_incorprtn=certfct_incorprtn.save(commit=False) 
        for aq in certfct_incorprtn:
            aq.contract = self.object
            aq.save()
        cmpny_profile_file=cmpny_profile_file.save(commit=False) 
        for aq in cmpny_profile_file:
            aq.contract = self.object
            aq.save()

        orgnztn_chart_formset=orgnztn_chart_formset.save(commit=False) 
        for aq in orgnztn_chart_formset:
            aq.contract = self.object
            aq.save()
        past_project_formset=past_project_formset.save(commit=False) 
        for aq in past_project_formset:
            aq.contract = self.object
            aq.save()
        formco2_formset=formco2_formset.save(commit=False) 
        for aq in formco2_formset:
            aq.contract = self.object
            aq.save()
        formco7_formset=formco7_formset.save(commit=False) 
        for aq in formco7_formset:
            aq.contract = self.object
            aq.save()
        form_co10_formset=form_co10_formset.save(commit=False) 
        for aq in form_co10_formset:
            aq.contract = self.object
            aq.save()
        dpr_formset=dpr_formset.save(commit=False) 
        for aq in dpr_formset:
            aq.contract = self.object
            aq.save()
        audit_formset=audit_formset.save(commit=False) 
        for aq in audit_formset:
            aq.contract = self.object
            aq.save()
        vat_formset=vat_formset.save(commit=False) 
        for aq in vat_formset:
            aq.contract = self.object
            aq.save()
        tax_formset=tax_formset.save(commit=False) 
        for aq in tax_formset:
            aq.contract = self.object
            aq.save()
        wcic_formset=wcic_formset.save(commit=False) 
        for aq in wcic_formset:
            aq.contract = self.object
            aq.save()
        cmpny_profile_formset=cmpny_profile_formset.save(commit=False) 
        for aq in cmpny_profile_formset:
            aq.contract = self.object
            aq.save()

        QMS_formset=QMS_formset.save(commit=False) 
        for aq in QMS_formset:
            aq.contract = self.object
            aq.save()

        # cmpny_profile_formset=cmpny_profile_formset.save(commit=False) 
        # for aq in cmpny_profile_formset:
        #     aq.contract = self.object
        #     aq.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, phone_formset, email_formset, website_formset, reg_ofc_formset,principal_formset,
        dir_formset,work_performance_formset,contact_formset,certfct_incorprtn,cmpny_profile_file,orgnztn_chart_formset,
        ast_project_formset,formco2_formset,formco7_formset,form_co10_formset,dpr_formset,audit_formset,vat_formset,
        tax_formset,wcic_formset,cmpny_profile_formset,QMS_formset):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.

        Args:
            form: Assignment Form
            assignment_question_form: Assignment Question Form
        """

        print "++++",form.errors

        return self.render_to_response(
                 self.get_context_data(form=form,phone_formset=phone_formset, email_formset=email_formset,
                                       website_formset=website_formset,reg_ofc_formset=reg_ofc_formset,
                                       principal_formset=principal_formset,dir_formset=dir_formset,
                                       work_performance_formset=work_performance_formset,contact_formset=contact_formset,
                                       certfct_incorprtn=certfct_incorprtn,cmpny_profile_file=cmpny_profile_file,orgnztn_chart_formset=orgnztn_chart_formset,
                                        past_project_formset=past_project_formset,formco2_formset=formco2_formset,formco7_formset=formco7_formset,
                                        form_co10_formset=form_co10_formset,dpr_formset=dpr_formset,audit_formset=audit_formset,vat_formset=vat_formset,
                                        tax_formset=tax_formset,wcic_formset=wcic_formset,cmpny_profile_formset=cmpny_profile_formset,QMS_formset=QMS_formset)
        )

        


class ContactUsView(TemplateView):
    template_name = 'contact_us.html'

class IndexView(View):
    template_name = 'index.html'
    success_url = '/'

    def post(self, *args, **kwrags):
        form.send_email()
        return super().form_valid(form)

class NewRegistration(FormView):
    form_class =  UserForm
    model = User
    template_name = 'registration.html'

    def get(self,request,*args,**kwargs):
        if not request.user.is_authenticated():
            self.object=None
            form_class=self.get_form_class()
            usr_form = self.get_form(form_class)
            reg_form = RegistrationForm()
            return self.render_to_response(self.get_context_data(form=usr_form,reg_form=reg_form))
        else:
            return HttpResponseRedirect(reverse('landing'))

    def post(self,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        usr_form = self.get_form(form_class)
        reg_form = RegistrationForm(self.request.POST)

        if (usr_form.is_valid() and reg_form.is_valid()):
            return self.form_valid(usr_form,reg_form)
        else:
            return self.form_invalid(usr_form,reg_form)

    def form_valid(self,usr_form,reg_form):
        email = usr_form.cleaned_data.get('email')
        company = reg_form.cleaned_data.get('company')
        user = User.objects.filter(username=email)
        if not user:
            self.object = usr_form.save(commit = False)
            self.object.is_staff = True
            self.object.username = email
            self.object.save()
            vendor1 = id_generator()
            vendor2 = random_with_N_digits(7)

            reg = reg_form.save(commit = False)
            reg.user = self.object
            vendor = "BELVEN"+str(vendor2)
            reg.vendor = vendor
            reg.save()
            self.created = True
            # email = EmailMessage('Subject', 'Body', to=[usr_form.ceaned_data.get('email')])
            raw_password = usr_form.cleaned_data.get('password1')
            html_message = loader.render_to_string(
                                'email/register.html',
                                {
                                    'email': email,
                                    'vendor': vendor,
                                    'company':company,
                                    'pwd':raw_password,
                                }
                            )
            try:
                send_mail('Thank you for registration !', 'message', settings.DEFAULT_FROM_EMAIL, [email],fail_silently=True,html_message=html_message)
            except Exception as e:
                print "+++++++++++e",e
            # email.send()
            username = usr_form.cleaned_data.get('email')
            
            # user = authenticate(username=username, password=raw_password)
            # login(self.request, user)
            messages.success(self.request, 'Thank you for registering, Kindly login or check your email for your username and password.')
            return HttpResponseRedirect(reverse('login'))
        else:
            messages.error(self.request, 'User with this email already exists')
            return self.render_to_response(self.get_context_data(form=usr_form,reg_form=reg_form))
        
    def form_invalid(self,usr_form,reg_form):
        print "form.errrr",usr_form.errors,reg_form.errors
        return self.render_to_response(self.get_context_data(form=usr_form,reg_form=reg_form))

    def get_success_url(self,**kwargs):
        return HttpResponseRedirect(reverse('landing'))


class SaveContactDetails(View):
    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subjt = request.POST.get('subject')
        message = request.POST.get('mesg')
        # print("ttttttttttttt",subjt,type(subjt))
        # if subjt=='0' and subjt=='1' :
        #     print("first>...................")
        #     subjt = 'I Would Like To Discuss'
        # elif subjt=='2':
        #     print("sssssssssssssssssssssss")
        #     subjt = 'I Would Like To Know About'
        # else:
        #     print("ttttttttttttttt")
        #     subjt = 'I Would Like To Suggest'
        print("in viewwwwwwwwwwwwwwwwwwwww",name,email,subjt,msg)
        contct_obj = ContactDetailsModel.objects.create(name=name,email=email,subject=subjt,message=message)
        return HttpResponse(json.dumps('success'), content_type='json')