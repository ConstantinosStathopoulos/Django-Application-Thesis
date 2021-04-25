from django.db import models
from accounts.models import Profile
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

# class Students(models.Model):


#Model for installments

class PaymentInstallment(models.Model):
    name = models.CharField(max_length=100, null=True)
    amount = models.DecimalField(max_digits=4, decimal_places=1)
    due_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.name


STATUS_CHOICES = (
    ("Accepted", "Accepted"),
    ("Denied", "Denied"),
    ("Pending", "Pending")
)




#Model for payments of students
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    installment = models.ForeignKey(PaymentInstallment, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    document = models.FileField(upload_to='student_payments/%Y/%m/%d/')
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'Pending'
        )
    


    def __str__(self):
        return '{self.user}_{self.installment}_{self.date}'.format(self=self)