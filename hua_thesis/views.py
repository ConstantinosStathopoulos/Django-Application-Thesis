from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from accounts.views import *
from student.views import *
from .decorators import unauthenticated_user
from django.urls import reverse
from office.models import Announcement
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


def home(request):
    return render(request, "home.html", {})


#for user logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

#implements the login
@unauthenticated_user
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        #redirect after login for type of user(student, professor, office etc)
        if user is not None:
            login(request, user)
            if user.profile.title == 'Μεταπτυχιακός Φοιτητής':
                return redirect('student_dashboard')
            elif user.profile.title == 'Αναπληρωτής Καθηγητής':
                return redirect('professor_dashboard')
            elif user.profile.title == 'Ιδρυματικός Λογαριασμός':
                return redirect(reverse('admin:index'))
        else:
            messages.info(request, 'Username OR password is incorrect')
        
    context = {}
    return render(request, 'login.html', context)

#for news view
def newsfeed(request):
    announcement = Announcement.objects.order_by('-date')
    context = {'announcement':announcement}
    return render(request, "newsfeed.html", context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            human = True
            subject = "Μήνυμα απο τη φόρμα επικοινωνίας της εφαρμογής του Π.Μ.Σ" 
            body = {
            'first_name': form.cleaned_data['first_name'], 
            'last_name': form.cleaned_data['last_name'], 
            'email': form.cleaned_data['email_address'], 
            'message':form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, ['it214100@hua.gr'], fail_silently=False) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("/contact/success/")
    form = ContactForm()

    return render(request, "contact.html", {'form':form})

def success(request):
    return render(request, "contact_success.html", {})