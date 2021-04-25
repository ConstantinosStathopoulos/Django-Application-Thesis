"""hua_thesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from student.views import *
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from hua_thesis.views import (
    user_login,
    user_logout,
    user_profile,
    newsfeed
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
    path('myprofile/', user_profile, name='profile'),
    path('newsfeed/', views.newsfeed, name='newsfeed'),
    path('student/my_dashboard', student_dashboard, name='student_dashboard'),
    path('professor/my_dashboard', professor_dashboard, name='professor_dashboard')
    # path('student/', include('student.urls'))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#to get file urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)