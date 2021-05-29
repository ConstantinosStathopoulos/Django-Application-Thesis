from django.contrib import admin
from django.urls import path, include
from student.views import *
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('my_dashboard', student_dashboard, name='student_dashboard'),
    path('payment/<str:pk>', payInstallment, name='pay_installment')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
