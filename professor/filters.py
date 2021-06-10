import django_filters
from django_filters import CharFilter

from .models import *

class FundingFilter(django_filters.FilterSet):
    
    class Meta:
        model = FundingRequisition
        fields = {
            'title': ['exact', 'contains'],
            'description': ['contains'],
            'status': ['exact'],
        }