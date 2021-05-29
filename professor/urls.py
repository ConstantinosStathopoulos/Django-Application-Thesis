from django.contrib import admin
from django.urls import path, include
from professor.views import *
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('my_dashboard', professor_dashboard, name='professor_dashboard'),
    path('new_funding_request', create_funding_request , name='create_funding_request'),
    path('new_speech_request', create_speech_request , name='create_speech_request')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#to get file urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)