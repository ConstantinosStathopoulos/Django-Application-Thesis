from django.db import models
from accounts.models import Profile
from datetime import datetime
from django.contrib.auth.models import User
from accounts.models import Student
import datetime
from django.utils.timezone import now
from django.utils import timezone

DUR_CHOICES = (
    ("Πλήρης Φοίτηση", "Πλήρης Φοίτηση"),
    ("Μερική Φοίτηση", "Μερική Φοίτηση")
)

YEAR_CHOICES = [
        (r,r) for r in range(2006, datetime.date.today().year+1)
    ]


class PaymentInstallment(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Όνομα')
    amount = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Ποσό')
    due_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name='Ημερομηνία Προθεσμίας')
    program_duration = models.CharField(max_length = 14, choices= DUR_CHOICES, default= "Πλήρης Φοίτηση", verbose_name='Διάρκεια Σπουδών')
    postgrad_year =  models.IntegerField(choices=YEAR_CHOICES, blank=True, null=True, default=datetime.datetime.now().year, verbose_name='Έτος Προγράμματος')

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
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Φοιτητής/ρια')
    installment = models.ForeignKey(PaymentInstallment, on_delete=models.CASCADE, verbose_name='Δόση')
    created_on = models.DateTimeField(default=timezone.now, blank=True, verbose_name='Ημερομηνία Δημιουργίας')
    updated_on = models.DateTimeField(auto_now=True, blank=True, verbose_name='Ημερομηνία Ενημέρωσης')
    document = models.FileField(upload_to=user_directory_path, verbose_name='Αρχείο')
    bank = models.CharField(max_length= 30,choices=BANK_CHOICES, blank=True, verbose_name='Τράπεζα')
    transaction_number = models.PositiveIntegerField(unique=True, help_text = 'Παρακαλώ εισάγετε τον 9ψήφιο κωδικό συναλλαγής', blank=True, verbose_name='Αριθμός Συναλλαγής')
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'Υπο Έλεγχο', 
        verbose_name='Κατάσταση'
        )
    

    #how the object will be represented in the admin page
    def __str__(self):
        return '{self.student}_{self.installment.name}'.format(self=self)
    
    class Meta:
        verbose_name = 'Πληρωμή Φοιτητή'
        verbose_name_plural = 'Πληρωμές Φοιτητών'