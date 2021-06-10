from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django.contrib import messages
from accounts.views import *
from student.views import *
from .decorators import unauthenticated_user
from django.urls import reverse
from office.models import Announcement


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


