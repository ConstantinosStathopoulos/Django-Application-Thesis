import django_filters
from django_filters import CharFilter,DateFilter

from .models import *
from django.contrib.postgres.forms.ranges import RangeWidget
from django.forms.widgets import DateInput, TextInput

class FundingFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="created_on", lookup_expr="gte",)
    end_date = DateFilter(field_name="created_on", lookup_expr="lte",)
    


    labels = {
            'title': 'Τίτλος',
            'description': 'Περιγραφή',
            'date_range': 'Διάστημα ημερομηνιών',
            'status': 'Κατάσταση',
        }

    class Meta:
        model = FundingRequisition
        fields = {
            'title': ['contains'],
            'description': ['contains'],
            'status': ['exact'],
            }


class SpeechFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="created_on", lookup_expr="gte")
    end_date = DateFilter(field_name="created_on", lookup_expr="lte")
    start_req_date = DateFilter(field_name="requested_date", lookup_expr="gte")
    end_req_date = DateFilter(field_name="requested_date", lookup_expr="lte")
    labels = {
            'title': 'Τίτλος',
            'description': 'Περιγραφή',
            'status': 'Κατάσταση',
            'date_range': 'Διάστημα Ημερομηνιών',
            'requested_date_range': 'Διάστημα Αιτηθέντων Ημερομηνιών',
        }

    class Meta:
        model = SpeechRequisition
        fields = {
            'title': ['contains'],
            'description': ['contains'],
            'status': ['exact'],
            }



class TravelFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="created_on", lookup_expr="gte")
    end_date = DateFilter(field_name="created_on", lookup_expr="lte")
    start_req_date = DateFilter(field_name="requested_date", lookup_expr="gte")
    end_req_date = DateFilter(field_name="requested_date", lookup_expr="lte")
    labels = {
            'title': 'Τίτλος',
            'description': 'Περιγραφή',
            'status': 'Κατάσταση',
            'date_range': 'Διάστημα Ημερομηνιών',
            'requested_date_range': 'Διάστημα Αιτηθέντων Ημερομηνιών',
        }

    class Meta:
        model = TravelRequisition
        fields = {
            'title': ['contains'],
            'description': ['contains'],
            'status': ['exact'],
            'location':['contains'],
            }