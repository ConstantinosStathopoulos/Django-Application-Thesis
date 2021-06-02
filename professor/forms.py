from django.forms import ModelForm
from .models import *
from django.http import request
from django import forms
from django.forms.widgets import DateTimeInput
from django.forms.fields import SplitDateTimeField




class FundingRequisitionForm(ModelForm):
    class Meta:
        model = FundingRequisition
        fields = ['title', 'description', 'amount']
        
        labels = {
        "title": "Τίτλος Ομιλίας",
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


class SpeechRequisitionForm(ModelForm):

    
    class Meta:
        model = SpeechRequisition
        fields = ['title', 'requested_date', 'description']

        labels = {
        "title": "Τίτλος Ομιλίας",
        "requested_date": "Αιτούμενη Ημερομηνία/Ώρα",
        "description": "Περιγραφή"
        }

        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Τίτλος της ομιλίας/σεμιναρίου'}),
        'requested_date': forms.SplitDateTimeWidget(date_attrs={'class': 'form-control','type': 'date'}, time_attrs={'class': 'form-control','type': 'time'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Κείμενο περιγραφής της ομιλίας/σεμιναρίου'}),
        }
