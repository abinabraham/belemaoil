# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class RegistrationModel(models.Model):
	user = models.OneToOneField(User)
	company = models.CharField(max_length=45)
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



class ContractorModel(models.Model):

	STATUS_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

	user = models.ForeignKey(User)
	company_name = models.CharField(max_length=45,null=False, blank=False)
	logo = models.FileField(upload_to='images')
	reg_no = models.CharField(max_length=45,null=False, blank=False)
	DPR_Permit_no = models.CharField(max_length=45,null=False, blank=False)
	TIN_no = models.CharField(max_length=45,null=False, blank=False)
	NIPEX_reg_status = models.CharField(max_length=45,choices=STATUS_CHOICES)

	def __str__(self):
		return self.company_name

	# contact = models.CharField(max_length=45,null=False, blank=False)
	# email = models.EmailField(null=False, blank=False)
	# website  = models.URLField(null=False, blank=False)
	# reg_office_address = models.TextField(blank=True, null=True)
	# principal_owner = models.CharField(max_length=45,null=False, blank=False)
	# annual_turnover = models.IntegerField(default=0)
	# state_equity = models.CharField(max_length=50,null=False,blank=False)
	# estimate_time = models.CharField(max_length=50,null=False,blank=False)
	# director_name = models.CharField(max_length=45,null=False, blank=False)
	# director_nationality = models.CharField(max_length=45,null=False, blank=False)
	# #work performance history
	# client_name = models.CharField(max_length=45,null=False, blank=False)
	# exectn_date = models.DateField(null=False, blank=False)
	# location = models.CharField(max_length=75,null=False, blank=False)
	# total_value_contract = models.IntegerField(null=False,blank=False)
	# client_contact_person = models.CharField(max_length=45,null=False, blank=False)
	# job_compltn_certificate  = models.FileField(upload_to='media/contrator/files')
	# state_origin = models.ForeignKey(StatesMaster,null=False, blank=False)
	# #contact person
	# contact_person_name = models.CharField(max_length=75,null=False, blank=False)
	# contact_person_email = models.EmailField(null=False, blank=False)
	# contact_person_phno= models.CharField(max_length=75,null=False, blank=False)
	# designation = models.CharField(max_length=75,null=False, blank=False)


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