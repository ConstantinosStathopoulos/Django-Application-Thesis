from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.db.models import Sum

# professor`s main dashboard menu view
@login_required
def professor_dashboard(request):
    user = request.user
    funding_requests = FundingRequisition.objects.filter(user=user).order_by('date')
    speech_requests = SpeechRequisition.objects.filter(user=user)
    fund_sum = FundingRequisition.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum']

    context = {
        'funding_requests':funding_requests,
        'speech_requests': speech_requests,
        'fund_sum': fund_sum,
    }

    
    return render(request, "professor_dashboard.html", context)

# View for Funding requests form
@login_required
def create_funding_request(request):

    form = FundingRequisitionForm()
    #to get data back from the form
    if request.method == "POST":
        form = FundingRequisitionForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.user = request.user
            user_form.save()
            return redirect('professor_dashboard')

    context = {
        'form': form
    }
    return render(request, 'professor_fund_request.html', context)

# View for Speech requests form
@login_required
def create_speech_request(request):
    form = SpeechRequisitionForm()
    #to get data back from the form
    if request.method == "POST":
        form = SpeechRequisitionForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.user = request.user
            user_form.save()
            return redirect('professor_dashboard')

    context = {
        'form': form
    }
    return render(request, 'professor_speech_request.html', context)