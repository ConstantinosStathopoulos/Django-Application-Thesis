from django.shortcuts import render
from .models import *

# Create your views here.

def professor_dashboard(request):
    user = request.user
    funding_requests = FundingRequisition.objects.filter(user=user)
    speech_requests = SpeechRequisition.objects.filter(user=user)

    context = {
        'funding_requests':funding_requests,
        'speech_requests': speech_requests,
    }

    return render(request, "professor_dashboard.html", context)