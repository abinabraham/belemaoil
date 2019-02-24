from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from models import *
from django.utils.translation import gettext as _



class GeneralPurposeForm(ModelForm):
    
    works =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label=_("Works"),
                                    choices=[(item.pk, item) for item in Works.objects.all()])
    maintenence =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label=_("maintenence"),
                                    choices=[(item.pk, item) for item in Maintenence.objects.all()])
    supply =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label=_("Supply"),
                                    choices=[(item.pk, item) for item in Supply.objects.all()])
    
    class Meta:
        model = GeneralPurpose
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(GeneralPurposeForm, self).__init__(*args, **kwargs)       
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'

class MajorCategoryForm(ModelForm):
    
    rehabcivil =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label=_("RehabCivil"),
                                    choices=[(item.pk, item) for item in RehabCivil.objects.all()])
    rehabmech =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label=_("RehabMech"),
                                    choices=[(item.pk, item) for item in RehabMech.objects.all()])
    rehabelectr =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label=_("RehabElectr"),
                                    choices=[(item.pk, item) for item in RehabElectr.objects.all()])
    general_suppl =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label=_("GeneralSupplies"),
                                    choices=[(item.pk, item) for item in GeneralSupplies.objects.all()])
    heat_prods =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label=_("HeatingCoolingProd"),
                                    choices=[(item.pk, item) for item in HeatingCoolingProd.objects.all()])
    safety_lab_prods =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label=_("SafetyLabChem"),
                                    choices=[(item.pk, item) for item in SafetyLabChem.objects.all()])
    mech_parts =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label=_("MechanicalParts"),
                                    choices=[(item.pk, item) for item in MechanicalParts.objects.all()])

    consultancy =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label=_("Consultancy"),
                                    choices=[(item.pk, item) for item in Consultancy.objects.all()])
    waterborehole =  forms.ChoiceField(label=_("WaterBoreHole"),
                                    choices=[(item.pk, item) for item in WaterBoreHole.objects.all()])
    protologi =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label=_("ProtocolLogistics"),
                                    choices=[(item.pk, item) for item in ProtocolLogistics.objects.all()])

    lab =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label=_("Laboratory"),
                                    choices=[(item.pk, item) for item in Laboratory.objects.all()])
    onshore =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label=_("OnshoreEnv"),
                                    choices=[(item.pk, item) for item in OnshoreEnv.objects.all()])

     
    
    class Meta:
        model = MajorCategory
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(MajorCategoryForm, self).__init__(*args, **kwargs)       
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input-sm'





