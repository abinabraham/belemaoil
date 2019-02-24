# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.



DEFAULT_COUNTRY_PK=1    
class CountryCodeMaster(models.Model):
    name_of_country = models.CharField(max_length=200, null=True, blank=True)
    country_code = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "{0}".format(self.country_code,self.name_of_country)

class RegistrationModel(models.Model):
    user = models.OneToOneField(User)
    company = models.CharField(max_length=45)
    country_code = models.ForeignKey(CountryCodeMaster,  default=DEFAULT_COUNTRY_PK)
    contact = models.CharField(max_length=45)
    vendor = models.CharField(max_length=45)
    created_on= models.DateTimeField(auto_now=True,null=False, blank=False)

    def __str__(self):
        return self.user.username


class ContactDetailsModel(models.Model):
    name = models.CharField(max_length=45,null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=100,null=False, blank=False)
    message = models.CharField(max_length=200,null=False, blank=False)  
    created_on= models.DateTimeField(auto_now=True,null=False, blank=False)

    def __str__(self):
        return self.name


class StatesMaster(models.Model):
    state = models.CharField("State Name",max_length=45,null=False, blank=False)
    created_on= models.DateTimeField(auto_now=True,null=False, blank=False)

    def __str__(self):
        return self.state

class ServiceCategory(models.Model):

  name = models.CharField(default='',max_length=100)

  def __unicode__(self):
          return "%s" % self.name
  class Meta:
    ordering = ['name']

class ContractorModel(models.Model):

    STATUS_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    # SERVICE_CATGRY_CHOICES = (
    #   ('Equipment Lease', 'Equipment Lease'),
    #   ('Oil Tools', 'Oil Tools'),
    #   ('Technology', 'Technology'),
    #   ('Oil Well Servicing', 'Oil Well Servicing'),

    # )

    user = models.ForeignKey(User)
    company_name = models.CharField(max_length=45,null=False, blank=False)
    logo = models.FileField(upload_to='images')
    reg_no = models.CharField(max_length=45,null=False, blank=False)
    DPR_Permit_no = models.CharField(max_length=45,null=False, blank=False)
    TIN_no = models.CharField(max_length=45,null=False, blank=False)
    NIPEX_reg_status = models.CharField(max_length=45,choices=STATUS_CHOICES)
    annual_turnover = models.IntegerField(default=0)
    state_equity = models.CharField(max_length=50,null=False,blank=False)
    estimate_time = models.CharField(max_length=50,null=False,blank=False)
    state_origin = models.ForeignKey(StatesMaster,null=False, blank=False)
    submission_date = models.DateTimeField(auto_now=True)
    signature = models.FileField(upload_to='media/contrator/files', null=True, blank= True)
    service_catgry = models.ManyToManyField(ServiceCategory,null=True, blank= True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.company_name


class PhoneNumber(models.Model):
    phonenumber = models.CharField(max_length=255)
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)
    def __str__(self):
        return self.phonenumber


class Email(models.Model):
    email = models.CharField(max_length=255)
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)
    def __str__(self):
        return self.email

class Website(models.Model):
    website = models.CharField(max_length=255)
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)
    def __str__(self):
        return self.website

class RegisteredOffice(models.Model):
    address = models.TextField(blank=True, null=True)
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)
    def __str__(self):
        return self.id

class PrincipalOwner(models.Model):
    partner = models.CharField(max_length=50,blank=True, null=True)
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return self.partner

class DirectorDetails(models.Model):
    dir_name = models.CharField(max_length=50,blank=True, null=True)
    dir_nationality = models.CharField(max_length=50,blank=True, null=True)
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return self.dir_name


class WorkPerformanceDetails(models.Model):
    client_name = models.CharField(max_length=45,null=False, blank=False)
    client_exectn_date = models.DateField(null=False, blank=False)
    location = models.CharField(max_length=75,null=False, blank=False)
    total_value_contract = models.IntegerField(null=False,blank=False)
    client_contact_person = models.CharField(max_length=45,null=False, blank=False)
    job_compltn_certificate  = models.FileField(upload_to='media/contrator/signatures')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return self.client_name



class ContactPersonDetails(models.Model):
    name = models.CharField(max_length=75,null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone= models.CharField(max_length=75,null=False, blank=False)
    designation = models.CharField(max_length=75,null=False, blank=False)
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return self.name


class CertificateIncorporation(models.Model):
    certi_file = models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)

class CompanyProfileFile(models.Model):
    company_profile_file = models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)



class OrganizationChart(models.Model):
    orgnztn_chart_file = models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)


class PastProjects(models.Model):
    pjt_file = models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)

class FormCO2(models.Model):
    co2_file = models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)


class FormCO7(models.Model):
    co7_file = models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)


class FormCO10(models.Model):
    c010_file = models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)


class DPRCertificate(models.Model):
    dpr_certi= models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)


class AuditAccount(models.Model):
    acc_file= models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)


class VATCertificate(models.Model):
    certificate= models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)


class CompanyTax(models.Model):
    tax_certifct= models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)


class WCIC(models.Model):
    wcic_file= models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)


class RefLetter(models.Model):
    ref_file= models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)


class CurrentITF(models.Model):
    citf= models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)


class NPLApp(models.Model):
    npl= models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)




class QMS(models.Model):
    iso_file= models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)


class HealthPolicy(models.Model):
    policy= models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)



class HealthCertificates(models.Model):
    cert= models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)


class OtherDoc(models.Model):
    doc= models.FileField(upload_to='media/contrator/files')
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return str(self.id)



class CompanyProfile(models.Model):
    STATUS_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    No_Of_Staff_CHOICES = (
        ('0 - 10', '0 - 10'),
        ('10 - 20', '10 - 20'),
    )

    duration = models.IntegerField(default=0,null=False, blank=False)
    no_of_staff = models.CharField(max_length=75,choices=No_Of_Staff_CHOICES)
    associated_status= models.CharField(max_length=75,choices=STATUS_CHOICES)
    associated_company = models.CharField(max_length=75)
    documents = models.FileField(upload_to='media/contrator/files')
    machinary_plants_status =  models.CharField(max_length=75,choices=STATUS_CHOICES)
    subsidiary_status = models.CharField(max_length=75,choices=STATUS_CHOICES)
    contract = models.ForeignKey(ContractorModel,null=False, blank=False)

    def __str__(self):
        return self.name














