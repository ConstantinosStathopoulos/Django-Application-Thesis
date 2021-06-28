from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hua_thesis.decorators import postgrad_student_required
from .models import *
from .forms import *
from accounts.models import Student
from django.db.models import Sum

# Create your views here.


@login_required
@postgrad_student_required
def student_dashboard(request):
    #Querysets
    
    student = request.user.profile.student
    #student payments
    student_payments = Payment.objects.filter(student=student).order_by('-created_on')
    #all the installments of the student, depending on program duration
    all_installments = PaymentInstallment.objects.filter(program_duration=student.program_duration, postgrad_year=student.postgrad_year).exclude(payment__in=student_payments, payment__status='Αποδεκτή').exclude(payment__in=student_payments, payment__status='Υπο Έλεγχο').order_by('due_date')
    #program price
    postgrad_price = PaymentInstallment.objects.filter(program_duration=student.program_duration, postgrad_year=student.postgrad_year).aggregate(Sum('amount'))['amount__sum']
    #paid amount
    paid_sum = PaymentInstallment.objects.filter(program_duration=student.program_duration, payment__in=student_payments).aggregate(Sum('amount'))['amount__sum']
    accepted_student_payments = Payment.objects.filter(student=student,status="Αποδεκτή")
    accepted_student_payments_sum = PaymentInstallment.objects.filter(program_duration=student.program_duration, payment__in=student_payments, payment__status="Αποδεκτή").aggregate(Sum('amount'))['amount__sum']
    declined_student_payments = Payment.objects.filter(student=student,status="Μη Αποδεκτή")
    pending_student_payments = Payment.objects.filter(student=student,status="Υπο Έλεγχο")



    context = {
        'student_payments':student_payments,
        'all_installments':all_installments,

        'postgrad_price':postgrad_price,
        'paid_sum':paid_sum,
        'accepted_student_payments': accepted_student_payments,
        'accepted_student_payments_sum': accepted_student_payments_sum,
        'declined_student_payments': declined_student_payments,
        'pending_student_payments': pending_student_payments,
        
    }

    return render(request, "student_dashboard.html", context)



@login_required
@postgrad_student_required
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



@login_required
@postgrad_student_required
def update_payment(request, pk):
    
    payment= Payment.objects.get(id=pk)
    form = PaymentForm(instance=payment)

    if request.method == "POST":
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('student_dashboard')
    context = {
        'form': form
    }
    return render(request, 'payment_form.html', context)



@login_required
@postgrad_student_required
def delete_payment(request, pk):
    
    payment= Payment.objects.get(id=pk)

    if request.method == "POST":
        payment.delete()
        return redirect('student_dashboard')
    context = {
        'payment': payment
    }
    return render(request, 'payment_form.html', context)