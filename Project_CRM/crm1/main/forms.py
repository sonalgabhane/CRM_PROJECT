# forms.py
from django import forms
from .models import *
from django.forms import modelformset_factory


class LeadForm(forms.ModelForm):
    class Meta:
        model=Lead
        fields = '__all__'
        # exclude = ["assigned"]


    def clean_leadno(self):
        leadno = self.cleaned_data['leadno']
        if not leadno:
            leadno = generate_lead_no()
        return leadno


    # def save(self, commit=True):
    #     lead = super().save(commit=False)
    #     if not Lead.leadno:
    #         Lead.leadno = generate_lead_no()
    #     if commit:
    #         lead.save()
    #     return lead


        
class SupplierForm(forms.ModelForm):
    class Meta:
        model=supplier
        # fields = "__all__"
        exclude = ["user"]
        
        
        
class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        # fields = "__all__"
        exclude = ('created_by','destinations')
        class Meta:
            widgets = {
                'mealtype' : forms.ChoiceField(choices=TAGS_CHOICES, widget=forms.RadioSelect()),
        }
            

# A regular form, not a formset
class BirdForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ["destination"]


BirdFormSet = modelformset_factory(Destination, fields=("destination",), extra=1)


# All Enquiry Type Forms

class FlightBookForm(forms.ModelForm):
    
    class Meta:
        model = FlightBook
        fields = '__all__'
        # widgets = {
        #     'leadno': forms.HiddenInput()
        # }

# class HotelBookForm(forms.ModelForm):
#     class Meta:
#         model = HotelBook
#         fields = '__all__'

# class VisaForm(forms.ModelForm):
#     class Meta:
#         model = Visa
#         fields = '__all__'

# class TravelInsuranceForm(forms.ModelForm):
#     class Meta:
#         model = TravelInsurance
#         fields = '__all__'

# class ForexForm(forms.ModelForm):
#     class Meta:
#         model = Forex
#         fields = '__all__'

# class SightseeingsForm(forms.ModelForm):
#     class Meta:
#         model = Sightseeings
#         fields = '__all__'

# class TransportForm(forms.ModelForm):
#     class Meta:
#         model = Transport
#         fields = '__all__'

# class OtherForm(forms.ModelForm):
#     class Meta:
#         model = Other
#         fields = '__all__'

# class PackageDetailsForm(forms.ModelForm):
#     class Meta:
#         model = PackageDetails
#         fields = '__all__'

# class CustomizePackageForm(forms.ModelForm):
#     class Meta:
#         model = CustomizePackage
#         fields = '__all__'

# class BusForm(forms.ModelForm):
#     class Meta:
#         model = Bus
#         fields = '__all__'

# class TrainForm(forms.ModelForm):
#     class Meta:
#         model = Train
#         fields = '__all__'

# class PassportForm(forms.ModelForm):
#     class Meta:
#         model = Passport
#         fields = '__all__'

# class CruiseForm(forms.ModelForm):
#     class Meta:
#         model = Cruise
#         fields = '__all__'

# class AdventureForm(forms.ModelForm):
#     class Meta:
#         model = Adventure
#         fields = '__all__'

# class GroupPackageForm(forms.ModelForm):
#     class Meta:
#         model = GroupPackage
#         fields = '__all__'


