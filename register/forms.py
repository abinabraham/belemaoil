from django import forms
from django.contrib.auth.forms import UserCreationForm

from models import RegistrationModel, PhoneNumber, Email, ContractorModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
from django.forms import formset_factory

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
        fields = ['company','contact']

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



class ContractorModelForm(ModelForm):
    class Meta:
        model = ContractorModel
        exclude = ('user',)

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



EmailFormSet = inlineformset_factory(ContractorModel,Email,
                                            form=EmailForm, extra=1)
PhoneNumberFormSet = inlineformset_factory(ContractorModel,PhoneNumber,
                                            form=PhoneNumberForm, extra=1)
WebsiteFormSet = inlineformset_factory(ContractorModel,Website,
                                            form=WebsiteForm, extra=1)

RegisteredOfficeFormSet = inlineformset_factory(ContractorModel,RegisteredOffice,
                                            form=RegisteredOfficeForm, extra=1)
