from django.contrib import admin
from django.urls import path, include
from student.views import *
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('my_dashboard', student_dashboard, name='student_dashboard'),
    path('new_payment/<str:pk>/', payInstallment, name='pay_installment'),
    path('update_payment/<str:pk>/', update_payment, name='update_payment'),
    path('delete_payment/<str:pk>/', delete_payment, name='delete_payment')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#to get file urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)