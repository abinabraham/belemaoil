from django import forms
from django.contrib.auth.forms import UserCreationForm

from models import RegistrationModel, PhoneNumber, Email, ContractorModel,PrincipalOwner,DirectorDetails
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
from django.forms import formset_factory

from models import *

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)       
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-lg'
            self.fields['first_name'].widget.attrs['placeholder']='First Name'
            self.fields['last_name'].widget.attrs['placeholder']='Last Name'
            self.fields['email'].widget.attrs['placeholder']='Email'
            self.fields['password1'].widget.attrs['placeholder']='Passowrd'
            self.fields['password2'].widget.attrs['placeholder']='Re-enter Password'

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = RegistrationModel
        fields = ['company','contact','country_code']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)       
        for field in self.fields:
            self.fields['contact'].widget.attrs['type']='number' 
            self.fields['company'].widget.attrs['placeholder']='Company Name' 
            self.fields['contact'].widget.attrs['placeholder']='Telephone' 

            self.fields[field].widget.attrs['class']='form-control input-lg'              
             

class RegistrationFormUniqueEmail(UserForm):
    """
    Subclass of ``RegistrationForm`` which enforces uniqueness of
    email addresses.
    """
    def __init__(self, *args, **kwargs):
        super(RegistrationFormUniqueEmail, self).__init__(*args, **kwargs)
        email_field = User.get_email_field_name()
        self.fields[email_field].validators.append(
            validators.CaseInsensitiveUnique(
                User, email_field,
                validators.DUPLICATE_EMAIL
            )
        )


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)       
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-lg'
            self.fields['username'].widget.attrs['placeholder']='Username'
            self.fields['password'].widget.attrs['placeholder']='Password'

# class PhoneNumberForm(forms.Form):

#     class Meta:
#         model = PhoneNumber
#         fields = ['__all__']

   


# PhoneNumberFormSet = formset_factory(PhoneNumberForm, extra=2, max_num=1)

from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from models import *
from django.utils.translation import gettext as _



class ContractorModelForm(ModelForm):
    
    service_catgry =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label=_("Services Category"),
                                    choices=[(item.pk, item) for item in ServiceCategory.objects.all()])
    class Meta:
        model = ContractorModel
        exclude = ('user','submission_date')

    def __init__(self, *args, **kwargs):
        super(ContractorModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'


class PhoneNumberForm(ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['phonenumber']

    def __init__(self, *args, **kwargs):
        super(PhoneNumberForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class WebsiteForm(ModelForm):
    class Meta:
        model = Website
        fields = ['website']

    def __init__(self, *args, **kwargs):
        super(WebsiteForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class RegisteredOfficeForm(ModelForm):
    class Meta:
        model = RegisteredOffice
        fields = ['address']

    def __init__(self, *args, **kwargs):
        super(RegisteredOfficeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class PrincipalOwnerForm(ModelForm):
    class Meta:
        model = PrincipalOwner
        fields = ['partner']

    def __init__(self, *args, **kwargs):
        super(PrincipalOwnerForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class DirectorDetailsForm(ModelForm):
    class Meta:
        model = DirectorDetails
        fields = ['dir_name','dir_nationality']

    def __init__(self, *args, **kwargs):
        super(DirectorDetailsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class WorkPerformanceDetailsForm(ModelForm):
    class Meta:
        model = WorkPerformanceDetails
        fields = ['client_exectn_date','location','total_value_contract','client_contact_person','job_compltn_certificate']

    def __init__(self, *args, **kwargs):
        super(WorkPerformanceDetailsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class ContactPersonDetailsForm(ModelForm):
    class Meta:
        model = ContactPersonDetails
        fields = ['name','email','phone','designation']

    def __init__(self, *args, **kwargs):
        super(ContactPersonDetailsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class CertificateIncorporationForm(ModelForm):
    class Meta:
        model = CertificateIncorporation
        fields = ['certi_file']

    def __init__(self, *args, **kwargs):
        super(CertificateIncorporationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class CompanyProfileFileForm(ModelForm):
    class Meta:
        model = CompanyProfileFile
        fields = ['company_profile_file']

    def __init__(self, *args, **kwargs):
        super(CompanyProfileFileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class OrganizationChartForm(ModelForm):
    class Meta:
        model = OrganizationChart
        fields = ['orgnztn_chart_file']

    def __init__(self, *args, **kwargs):
        super(OrganizationChartForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class PastProjectsForm(ModelForm):
    class Meta:
        model = PastProjects
        fields = ['pjt_file']

    def __init__(self, *args, **kwargs):
        super(PastProjectsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class FormCO2Form(ModelForm):
    class Meta:
        model = FormCO2
        fields = ['co2_file']

    def __init__(self, *args, **kwargs):
        super(FormCO2Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class FormCO7Form(ModelForm):
    class Meta:
        model = FormCO7
        fields = ['co7_file']

    def __init__(self, *args, **kwargs):
        super(FormCO7Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class FormCO10Form(ModelForm):
    class Meta:
        model = FormCO10
        fields = ['c010_file']

    def __init__(self, *args, **kwargs):
        super(FormCO10Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class DPRCertificateForm(ModelForm):
    class Meta:
        model = DPRCertificate
        fields = ['dpr_certi']

    def __init__(self, *args, **kwargs):
        super(DPRCertificateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class AuditAccountForm(ModelForm):
    class Meta:
        model = AuditAccount
        fields = ['acc_file']

    def __init__(self, *args, **kwargs):
        super(AuditAccountForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class VATCertificateForm(ModelForm):
    class Meta:
        model = VATCertificate
        fields = ['certificate']

    def __init__(self, *args, **kwargs):
        super(VATCertificateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class CompanyTaxForm(ModelForm):
    class Meta:
        model = CompanyTax
        fields = ['tax_certifct']

    def __init__(self, *args, **kwargs):
        super(CompanyTaxForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class WCICForm(ModelForm):
    class Meta:
        model = WCIC
        fields = ['wcic_file']

    def __init__(self, *args, **kwargs):
        super(WCICForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class RefLetterForm(ModelForm):
    class Meta:
        model = RefLetter
        fields = ['ref_file']

    def __init__(self, *args, **kwargs):
        super(RefLetterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class NPLAppForm(ModelForm):
    class Meta:
        model = NPLApp
        fields = ['npl']

    def __init__(self, *args, **kwargs):
        super(NPLAppForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class CurrentITFForm(ModelForm):
    class Meta:
        model = CurrentITF
        fields = ['citf']

    def __init__(self, *args, **kwargs):
        super(CurrentITFForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'


class CompanyProfileForm(ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['duration','no_of_staff','associated_status','associated_company','documents','machinary_plants_status','subsidiary_status']

    def __init__(self, *args, **kwargs):
        super(CompanyProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'


  
class HealthSafetyForm(ModelForm):
    class Meta:
        model = HealthCertificates
        fields = ['cert']

    def __init__(self, *args, **kwargs):
        super(HealthSafetyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class HealthPolicyForm(ModelForm):
    class Meta:
        model = HealthPolicy
        fields = ['policy']

    def __init__(self, *args, **kwargs):
        super(HealthPolicyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class OtherDocForm(ModelForm):
    class Meta:
        model = OtherDoc
        fields = ['doc']

    def __init__(self, *args, **kwargs):
        super(OtherDocForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'



class QMSForm(ModelForm):
    class Meta:
        model = QMS
        fields = ['iso_file']

    def __init__(self, *args, **kwargs):
        super(QMSForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

EmailFormSet = inlineformset_factory(ContractorModel,Email,
                                            form=EmailForm, extra=1)
PhoneNumberFormSet = inlineformset_factory(ContractorModel,PhoneNumber,
                                            form=PhoneNumberForm, extra=1)
WebsiteFormSet = inlineformset_factory(ContractorModel,Website,
                                            form=WebsiteForm, extra=1)

RegisteredOfficeFormSet = inlineformset_factory(ContractorModel,RegisteredOffice,
                                            form=RegisteredOfficeForm, extra=1)

PrincipalOwnerFormSet = inlineformset_factory(ContractorModel,PrincipalOwner,
                                            form=PrincipalOwnerForm, extra=1)

DirectorDetailsFormSet = inlineformset_factory(ContractorModel,DirectorDetails,
                                            form=DirectorDetailsForm, extra=1)

WorkPerformanceDetailsFormSet = inlineformset_factory(ContractorModel,WorkPerformanceDetails,
                                            form=WorkPerformanceDetailsForm, extra=1)

ContactPersonDetailsFormSet = inlineformset_factory(ContractorModel,ContactPersonDetails,
                                            form=ContactPersonDetailsForm, extra=1)

CertificateIncorporationFormSet = inlineformset_factory(ContractorModel,CertificateIncorporation,
                                            form=CertificateIncorporationForm, extra=1)

CompanyProfileFileFormSet = inlineformset_factory(ContractorModel,CompanyProfileFile,
                                            form=CompanyProfileFileForm, extra=1)

OrganizationChartFormSet = inlineformset_factory(ContractorModel,OrganizationChart,form=OrganizationChartForm, extra=1)
PastProjectsFormSet = inlineformset_factory(ContractorModel,PastProjects,form=PastProjectsForm, extra=1)
FormCO2FormSet = inlineformset_factory(ContractorModel,FormCO2,form=FormCO2Form, extra=1)
FormCO7FormSet = inlineformset_factory(ContractorModel,FormCO7,form=FormCO7Form, extra=1)
FormCO10FormSet = inlineformset_factory(ContractorModel,FormCO10,form=FormCO10Form, extra=1)
DPRCertificateFormSet = inlineformset_factory(ContractorModel,DPRCertificate,form=DPRCertificateForm, extra=1)
AuditAccountFormSet =  inlineformset_factory(ContractorModel,AuditAccount,form=AuditAccountForm, extra=1)
VATCertificateFormSet =  inlineformset_factory(ContractorModel,VATCertificate,form=VATCertificateForm, extra=1)
CompanyTaxFormSet =  inlineformset_factory(ContractorModel,CompanyTax,form=CompanyTaxForm, extra=1)
WCICFormSet =  inlineformset_factory(ContractorModel,WCIC,form=WCICForm, extra=1)
CompanyProfileFormSet =  inlineformset_factory(ContractorModel,CompanyProfile,form=CompanyProfileForm, extra=1)
QMS_formset =  inlineformset_factory(ContractorModel,QMS,form=QMSForm, extra=1)


RefLetterFormSet =  inlineformset_factory(ContractorModel,RefLetter,form=RefLetterForm, extra=1)
NPLAppFormSet =  inlineformset_factory(ContractorModel,NPLApp,form=NPLAppForm, extra=1)
CurrentITFFormSet =  inlineformset_factory(ContractorModel,CurrentITF,form=CurrentITFForm, extra=1)
HealthPolicyFormSet =  inlineformset_factory(ContractorModel,HealthPolicy,form=HealthPolicyForm, extra=1)
HealthSafetyFormFormSet =  inlineformset_factory(ContractorModel,HealthCertificates,form=HealthSafetyForm, extra=1)
OtherDocFormFormSet =  inlineformset_factory(ContractorModel,OtherDoc,form=OtherDocForm, extra=1)



