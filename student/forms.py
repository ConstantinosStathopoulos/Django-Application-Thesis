from django.forms import ModelForm
from .models import *
from django.http import request
from django import forms


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['bank','transaction_number','document']

        labels = {
        "bank": "Τράπεζα Συναλαγής",
        "transaction_number": "Κωδικός Συναλαγής",
        "document": "Αρχείο Απόδειξης"
        }