from django.forms import ModelForm
from .models import *
from django.http import request
from django import forms
from django.forms.widgets import DateTimeInput
from django.forms.fields import SplitDateTimeField
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminSplitDateTime



# form for Fund request
class FundingRequisitionForm(ModelForm):
    class Meta:
        model = FundingRequisition
        fields = ['title', 'description', 'amount']
        
        labels = {
        "title": "Τίτλος Αίτησης",
        "description": "Περιγραφή",
        "amount": "Αιτούμενο Ποσό"
        }
        
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Τίτλος αίτησης'}),
        'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Κείμενο περιγραφής του λόγου αίτησης χρηματοδότησης'}),
        }
class DateInput(forms.DateInput):
    input_type = 'date'


# form for Speech request
class SpeechRequisitionForm(ModelForm):
    
    
    class Meta:
        model = SpeechRequisition
        fields = ['title', 'requested_date','requested_time', 'description']

        labels = {
        "title": "Τίτλος Αίτησης",
        "requested_date": "Αιτούμενη Ημερομηνία",
        "requested_time": "Αιτούμενη Ώρα",
        "description": "Περιγραφή"
        }

        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Τίτλος της ομιλίας/σεμιναρίου'}),
        'requested_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder':'π.χ 25/06/2021', 'type': 'date'}, format=('%d/%m/%Y')),
        'requested_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Κείμενο περιγραφής της ομιλίας/σεμιναρίου'}),
        }

    def clean_date(self):
        requested_date = self.cleaned_data['date']
        if requested_date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return requested_date
    

class TravelRequisitionForm(ModelForm):
    
    
    class Meta:
        model = TravelRequisition
        fields = ['title', 'requested_date', 'travel_fees', 'accommodation_fees', 'registration_fees', 'location','description']

        labels = {
        "title": "Τίτλος Αίτησης",
        "requested_date": "Αιτούμενη Ημερομηνία/Ώρα",
        "travel_fees": "Έξοδα Μετακίνησης",
        "accommodation_fees":"Έξοδα Διαμονής",
        "registration_fees": "Έξοδα Εγγραφής",
        "location": "Τοποθεσία",
        "description": "Περιγραφή"
        }

        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Τίτλος της αίτησης'}),
        'requested_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'},format= ('%d/%m/%Y')),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Κείμενο περιγραφής της μετακίνησης για επαγγελματικό ταξίδι.'}),
        }