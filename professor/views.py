from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hua_thesis.decorators import professor_required
from .models import *
from .forms import *
from django.db.models import Sum
from .filters import FundingFilter, SpeechFilter, TravelFilter

# professor`s main dashboard menu view
@login_required
@professor_required
def professor_dashboard(request):
    user = request.user
    funding_requests = FundingRequisition.objects.filter(user=user).order_by('-created_on')
    speech_requests = SpeechRequisition.objects.filter(user=user).order_by('-created_on')
    travel_requests = TravelRequisition.objects.filter(user=user).order_by('-created_on')
    
    #general info
    
    
    num_of_fund_requests =FundingRequisition.objects.filter(user=user).count()
    num_of_speech_requests =SpeechRequisition.objects.filter(user=user).count()
    num_of_travel_requests =TravelRequisition.objects.filter(user=user).count()
    accepted_funding_requests = funding_requests.filter(status="Αποδεκτή")
    declined_funding_requests = funding_requests.filter(status="Μη Αποδεκτή")
    accepted_speech_requests = speech_requests.filter(status="Αποδεκτή")
    declined_speech_requests = speech_requests.filter(status="Μη Αποδεκτή")
    accepted_travel_requests = travel_requests.filter(status="Αποδεκτή")
    declined_travel_requests = travel_requests.filter(status="Μη Αποδεκτή")


    fund_sum = FundingRequisition.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum']
    accepted_fund = FundingRequisition.objects.filter(user=user, status="Αποδεκτή").aggregate(Sum('amount'))['amount__sum']
    
    
    #filters
    fundFilter = FundingFilter(request.GET, queryset=funding_requests)
    funding_requests = fundFilter.qs

    speech_filter = SpeechFilter(request.GET, queryset=speech_requests)
    speech_requests = speech_filter.qs

    travel_filter = TravelFilter(request.GET, queryset=travel_requests)
    travel_requests = travel_filter.qs

    context = {
        'funding_requests':funding_requests,
        'speech_requests': speech_requests,
        'travel_requests': travel_requests,

        'fundFilter': fundFilter,
        'speech_filter': speech_filter,
        'travel_filter': travel_filter,

        'fund_sum': fund_sum,
        'accepted_fund': accepted_fund,
        'num_of_fund_requests': num_of_fund_requests,
        'num_of_speech_requests': num_of_speech_requests,
        'num_of_travel_requests': num_of_travel_requests,
        'accepted_funding_requests': accepted_funding_requests,
        'declined_funding_requests': declined_funding_requests,
        'accepted_speech_requests' : accepted_speech_requests,
        'declined_speech_requests' : declined_speech_requests,
        'accepted_travel_requests' : accepted_travel_requests,
        'declined_travel_requests' : declined_travel_requests,

    }

    
    return render(request, "professor_dashboard.html", context)

# View for Funding requests form
@login_required
@professor_required
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
@professor_required
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

#CRUD for fund requests

#view to update pending fund requests
@login_required
@professor_required
def update_funding_request(request, pk):
    
    fund_request = FundingRequisition.objects.get(id=pk)
    form = FundingRequisitionForm(instance=fund_request)

    if request.method == "POST":
        form = FundingRequisitionForm(request.POST, instance=fund_request)
        if form.is_valid():
            form.save()
            return redirect('professor_dashboard')
    context = {
        'form': form
    }
    return render(request, 'professor_fund_request.html', context)




#view to delete funding requests of professor
@login_required
@professor_required
def delete_funding_request(request, pk):

    fund_request = FundingRequisition.objects.get(id=pk)
    if request.method == "POST":
        fund_request.delete()
        return redirect('professor_dashboard')
    context = {
        'fund_request':fund_request
    }
    return render(request, 'delete_fund_request.html', context)





#CRUD for speech requests



#view to update pending speech requests
@login_required
@professor_required
def update_speech_request(request, pk):
    
    speech_request = SpeechRequisition.objects.get(id=pk)
    form = SpeechRequisitionForm(instance=speech_request)

    if request.method == "POST":
        form = SpeechRequisitionForm(request.POST, instance=speech_request)
        if form.is_valid():
            form.save()
            return redirect('professor_dashboard')
    context = {
        'form': form
    }
    return render(request, 'professor_speech_request.html', context)




#view to delete speech requests of professor
@login_required
@professor_required
def delete_speech_request(request, pk):

    speech_request = SpeechRequisition.objects.get(id=pk)
    if request.method == "POST":
        speech_request.delete()
        return redirect('professor_dashboard')
    context = {
        'speech_request':speech_request
    }
    return render(request, 'delete_speech_request.html', context)



#CRUD for travel requests

# View for Travel requests form
@login_required
@professor_required
def create_travel_request(request):
    form = TravelRequisitionForm()
    #to get data back from the form
    if request.method == "POST":
        form = TravelRequisitionForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.user = request.user
            user_form.save()
            return redirect('professor_dashboard')

    context = {
        'form': form
    }
    return render(request, 'professor_travel_request.html', context)


#view to update pending travel requests
@login_required
@professor_required
def update_travel_request(request, pk):
    
    travel_request = TravelRequisition.objects.get(id=pk)
    form = TravelRequisitionForm(instance=travel_request)

    if request.method == "POST":
        form = TravelRequisitionForm(request.POST, instance=travel_request)
        if form.is_valid():
            form.save()
            return redirect('professor_dashboard')
    context = {
        'form': form
    }
    return render(request, 'professor_travel_request.html', context)




#view to delete travel requests of professor
@login_required
@professor_required
def delete_travel_request(request, pk):

    travel_request = TravelRequisition.objects.get(id=pk)
    if request.method == "POST":
        travel_request.delete()
        return redirect('professor_dashboard')
    context = {
        'travel_request':travel_request
    }
    return render(request, 'delete_travel_request.html', context)
