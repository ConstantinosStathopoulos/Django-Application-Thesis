from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django.contrib import messages
from accounts.views import *
from student.views import *

def home(request):
    return render(request, "home.html", {})


#for user logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

#implements the login
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
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
                else:
                    return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
            
        context = {}
        return render(request, 'login.html', context)

#for news view
def newsfeed(request):
    return render(request, "newsfeed.html", {})


