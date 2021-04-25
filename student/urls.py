from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from student.views import student_dashboard
from django.views.generic.base import TemplateView
from django.conf import settings

urlpatterns = [
    # path('student/my_dashboard', student_dashboard, name='student_dashboard'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
