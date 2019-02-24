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
from django.views import generic
from binascii import a2b_base64

from django.core.files.base import ContentFile


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return str(''.join(random.choice(chars) for _ in range(size)))

class LandingPageView(generic.FormView):
    form_class = ContractorModelForm
    template_name = 'landing.html'
    success_url = '/index/'
    model = ContractorModel
    context_object_name = 'contract'



    phone_formset = PhoneNumberFormSet
    email_formset = EmailFormSet
    website_formset = WebsiteFormSet
    reg_ofc_formset = RegisteredOfficeFormSet
    principal_formset=PrincipalOwnerFormSet
    dir_formset=DirectorDetailsFormSet
    work_performance_formset = WorkPerformanceDetailsFormSet
    contact_formset = ContactPersonDetailsFormSet
    certfct_incorprtn = CertificateIncorporationFormSet
    cmpny_profile_file = CompanyProfileFileFormSet
    orgnztn_chart_formset=OrganizationChartFormSet
    past_project_formset = PastProjectsFormSet
    formco2_formset = FormCO2FormSet
    formco7_formset = FormCO7FormSet
    form_co10_formset = FormCO10FormSet
    dpr_formset = DPRCertificateFormSet
    audit_formset = AuditAccountFormSet
    vat_formset = VATCertificateFormSet
    tax_formset = CompanyTaxFormSet
    wcic_formset = WCICFormSet
    ref_formset = RefLetterFormSet
    npl_formset = NPLAppFormSet
    citf_formset = CurrentITFFormSet
    hcert_formset = HealthSafetyFormFormSet
    hpolicy_formset = HealthPolicyFormSet
    other_formset = OtherDocFormFormSet        
    QMS_formset = QMS_formset
    cmpny_profile_formset = CompanyProfileFormSet

    def __init__(self, *args, **kwargs):
        super(LandingPageView, self).__init__(*args, **kwargs)
        self.formsets = {                        
                        'phone_formset': self.phone_formset,
                        'email_formset': self.email_formset,
                        'website_formset': self.website_formset,
                        'reg_ofc_formset': self.reg_ofc_formset,
                        'principal_formset': self.principal_formset,
                        'dir_formset': self.dir_formset,
                        'work_performance_formset':self.work_performance_formset,
                        'contact_formset': self.contact_formset,
                        'certfct_incorprtn' : self.certfct_incorprtn,
                        'cmpny_profile_file': self.cmpny_profile_file,
                        'orgnztn_chart_formset': self.orgnztn_chart_formset,
                        'past_project_formset' : self.past_project_formset,
                        'formco2_formset' : self.formco2_formset,
                        'formco7_formset' : self.formco7_formset,
                        'form_co10_formset': self.form_co10_formset,
                        'dpr_formset' : self.dpr_formset,
                        'audit_formset' : self.audit_formset,
                        'vat_formset' : self.vat_formset,
                        'tax_formset': self.tax_formset,
                        'wcic_formset': self.wcic_formset,
                        'ref_formset' : self.ref_formset,
                        'npl_formset' : self.npl_formset,
                        'citf_formset' : self.citf_formset,
                        'hcert_formset' : self.hcert_formset,
                        'hpolicy_formset' : self.hpolicy_formset,
                        'other_formset' : self.other_formset,    
                        'QMS_formset' : self.QMS_formset,
                        'cmpny_profile_formset' : self.cmpny_profile_formset,
                         }


    def get_context_data(self, **kwargs):
        ctx = super(LandingPageView, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ctx['form'] = form
        try:
            data_ob = RegistrationModel.objects.get(user=self.request.user)
        except:data_ob=None
        ctx['data_ob'] = data_ob

        

        for ctx_name, formset_class in self.formsets.items():
            if ctx_name not in ctx:
                ctx[ctx_name] = formset_class()
        return ctx


    def clean(self, form, formsets):
        """
        Perform any cross-form/formset validation. If there are errors, attach
        errors to a form or a form field so that they are displayed to the user
        and return False. If everything is valid, return True. This method will
        be called regardless of whether the individual forms are valid.
        """
        return True

    

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        data_uri = request.POST.get("signature")


        formsets = {}
        for ctx_name, formset_class in self.formsets.items():
            formsets[ctx_name] = formset_class(
                                               self.request.POST,
                                               self.request.FILES)

        is_valid = form.is_valid() and all([formset.is_valid()
                                            for formset in formsets.values()])

        cross_form_validation_result = self.clean(form, formsets)
        if is_valid and cross_form_validation_result:
            return self.form_valid(form, formsets, data_uri)
        else:
            return self.form_invalid(form, formsets, data_uri)


    def form_valid(self, form, formsets, data_uri):
        """
        Called if all forms are valid. Creates Assignment instance along with the
        associated AssignmentQuestion instances then redirects to success url
        Args:
            form: Assignment Form
            assignment_question_form: Assignment Question Form

        Returns: an HttpResponse to success url

        """

        data_uri = data_uri
        head, data = data_uri.split(',')
        binary_data = a2b_base64(data)


        self.object = form.save(commit=False)
        self.object.signature.save('sign_'+self.request.user.username+'.jpg', ContentFile(binary_data), save=False)
        self.object.user = self.request.user
        self.object.save()




        for formset in formsets.values():
            formset_ob = formset.save(commit=False)
            for aq in formset_ob:
                aq.contract = self.object
                aq.save()

        messages.success(self.request, 'Thank you for submitting details. Will prcoess and let you know the status.')
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formsets, data_uri):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.

        """
        for formset in formsets.values():
            if formset.errors[0]:
                messages.error(self.request, formset.errors[0])  
        return self.render_to_response(
                 self.get_context_data(form=form,**formsets))

        


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
            subject = 'Thank you for registering'
            message = 'Thank you for registering'
            email_from = "Belemaoil <no_reply@belemaoil.com >"
            recipient_list = [email]
            try:
                send_mail(subject, message, email_from, recipient_list,fail_silently=False,html_message=html_message)
            except Exception as e:
                raise Exception('{}'.format(e))
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
        print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
        name = request.POST.get('name')
        email = request.POST.get('email')
        subjt = request.POST.get('subject')
        message = request.POST.get('message')
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
        # print("in viewwwwwwwwwwwwwwwwwwwww",name,email,subjt,msg)
        contct_obj = ContactDetailsModel.objects.create(name=name,email=email,subject=subjt,message=message)
        return HttpResponse(json.dumps('success'), content_type='json')