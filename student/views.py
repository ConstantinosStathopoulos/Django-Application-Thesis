from django.shortcuts import render
from .models import *
# Create your views here.


def student_dashboard(request):

    student_payments = Payment.objects.all()
    all_installments = PaymentInstallment.objects.all()
    context = {
        'student_payments':student_payments,
        'all_installments':all_installments,
    }

    return render(request, "student_dashboard.html", context)

# def professor_dashboard(request):
#     return render(request, "professor_dashboard.html", {})