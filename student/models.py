from django.db import models
from accounts.models import Profile
from datetime import datetime
from django.contrib.auth.models import User
from accounts.models import Student


DUR_CHOICES = (
    ("Πλήρης Φοίτηση", "Πλήρης Φοίτηση"),
    ("Μερική Φοίτηση", "Μερική Φοίτηση")
)


class PaymentInstallment(models.Model):
    name = models.CharField(max_length=100, null=True)
    amount = models.DecimalField(max_digits=4, decimal_places=1)
    due_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    program_duration = models.CharField(max_length = 14, choices= DUR_CHOICES, default= "Πλήρης Φοίτηση")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Δόση Μεταπτυχιακού'
        verbose_name_plural = 'Δόσεις Μεταπτυχιακού'



#status choices for payments
STATUS_CHOICES = (
    ("Αποδεκτή", "Αποδεκτή"),
    ("Μη Αποδεκτή", "Μη Αποδεκτή"),
    ("Υπο Έλεγχο", "Υπο Έλεγχο")
)

BANK_CHOICES = (
    ("Εθνική Τράπεζα", "Εθνική Τράπεζα"),
    ("Πειραιώς", "Πειραιώς"),
    ("Eurobank", "Eurobank"),
    ("Alpha Bank", "Alpha Bank")
    )


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<username>/<installment_name>_<filename>
    return 'user_{0}/{1}_{2}'.format(instance.student.profile.user.username, instance.installment.name, filename)





#Model for payments of students
class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    installment = models.ForeignKey(PaymentInstallment, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    document = models.FileField(upload_to=user_directory_path)
    bank = models.CharField(max_length= 30,choices=BANK_CHOICES, blank=True)
    transaction_number = models.PositiveIntegerField( blank=True)
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'Υπο Έλεγχο'
        )
    

    #how the object will be represented in the admin page
    def __str__(self):
        return '{self.student}_{self.installment}_{self.date}'.format(self=self)
    
    class Meta:
        verbose_name = 'Πληρωμή Φοιτητή'
        verbose_name_plural = 'Πληρωμές Φοιτητών'