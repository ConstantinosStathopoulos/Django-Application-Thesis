from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from accounts.models import Student
# Create your views here.


@login_required
def student_dashboard(request):
    #Querysets
    
    student = request.user.profile.student
    #student payments
    student_payments = Payment.objects.filter(student=student)
    #all the installments of the student, depending on program duration
    all_installments = PaymentInstallment.objects.filter(program_duration=student.program_duration).exclude(payment__in=student_payments)
    #current debt




    context = {
        'student_payments':student_payments,
        'all_installments':all_installments,
    }

    return render(request, "student_dashboard.html", context)



@login_required
def payInstallment(request, pk):

    installment = PaymentInstallment.objects.get(id=pk)
    form = PaymentForm(instance=installment)

    if request.method == 'POST':
        form = PaymentForm(request.POST,request.FILES)
        if form.is_valid():
            payform = form.save(commit=False)
            payform.student = request.user.profile.student
            payform.installment = installment
            payform.save()
            return redirect('student_dashboard')
    else:
        form = PaymentForm()
    context = {'form':form}

    return render(request, "payment_form.html", context)