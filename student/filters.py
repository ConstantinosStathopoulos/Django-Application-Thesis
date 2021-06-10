import django_filters
# from django_filters.views import FilterView
from django_filters import CharFilter

from .models import *

class PaymentFilter(django_filters.FilterSet):
    
    class Meta:
        model = Payment
        fields = {
            'bank': ['exact'],
            'transaction_number': ['contains'],
            'status': ['exact'],
        }
        