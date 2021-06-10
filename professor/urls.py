from django.contrib import admin
from django.urls import path, include
from professor.views import *
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('my_dashboard', professor_dashboard, name='professor_dashboard'),
    #speech urls
    path('new_speech_request', create_speech_request , name='create_speech_request'),
    path('update_speech_request/<str:pk>/', update_speech_request, name='update_speech_request'),
    path('delete_speech_request/<str:pk>/', delete_speech_request, name='delete_speech_request'),
    #funding urls
    path('new_funding_request', create_funding_request , name='create_funding_request'),
    path('update_fund_request/<str:pk>/', update_funding_request, name='update_funding_request'),
    path('delete_fund_request/<str:pk>/', delete_funding_request, name='delete_funding_request'),
    #travel urls
    path('create_travel_request', create_travel_request , name='create_travel_request'),
    path('update_travel_request/<str:pk>/', update_travel_request, name='update_travel_request'),
    path('delete_travel_request/<str:pk>/', delete_travel_request, name='delete_travel_request'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#to get file urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)