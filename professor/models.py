from django.db import models
from accounts.models import Profile
from datetime import datetime
from django.contrib.auth.models import User


STATUS_CHOICES = (
    ("Αποδεκτή", "Αποδεκτή"),
    ("Μη Αποδεκτή", "Μη Αποδεκτή"),
    ("Υπο Έλεγχο", "Υπο Έλεγχο")
)



class FundingRequisition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Χρήστης')
    title = models.CharField(max_length=200, blank=False, verbose_name='Τίτλος')
    created_on = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Ημερομηνία Δημιουργίας')
    updated_on = models.DateTimeField(auto_now=True, blank=True, verbose_name='Ημερομηνία Ενημέρωσης')
    description = models.TextField(blank=False, verbose_name='Περιγραφή')
    amount = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Ποσό')
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'Υπο Έλεγχο',
        verbose_name='Κατάσταση'
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Αίτηση Χρηματοδότησης'
        verbose_name_plural = 'Αιτήσεις Χρηματοδότησης'





class SpeechRequisition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Χρήστης')
    title = models.CharField(max_length=200, blank=False, verbose_name='Τίτλος')
    created_on = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Ημερομηνία Δημιουργίας')
    updated_on = models.DateTimeField(auto_now=True, blank=True, verbose_name='Ημερομηνία Ενημέρωσης')
    requested_date = models.DateField(verbose_name="Αιτούμενη Ημερομηνία", help_text="Εισάγετε την Ημερομηνία της Ομιλίας/Εκδήλωσης")
    requested_time = models.TimeField(verbose_name="Αιτούμενη Ώρα", help_text="Εισάγετε την Ώρα της Ομιλίας/Εκδήλωσης")
    description = models.TextField(blank=False, verbose_name='Περιγραφή')
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'Υπο Έλεγχο',
        verbose_name='Κατάσταση'
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Αίτηση Εκδήλωσης'
        verbose_name_plural = 'Αιτήσεις Εκδήλωσης'



class TravelRequisition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Χρήστης')
    title = models.CharField(max_length=200, blank=False, verbose_name='Τίτλος')
    created_on = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Ημερομηνία Δημιουργίας')
    updated_on = models.DateTimeField(auto_now=True, blank=True, verbose_name='Ημερομηνία Ενημέρωσης')
    requested_date = models.DateField(verbose_name="Αιτούμενη Ημερομηνία")
    description = models.TextField(blank=False, verbose_name='Περιγραφή')
    travel_fees = models.DecimalField(max_digits=6, decimal_places=1, blank=False, verbose_name='Ποσό Ταξιδιού')
    accommodation_fees = models.DecimalField(max_digits=6, decimal_places=1,blank=False, verbose_name='Ποσό Διαμονής')
    registration_fees = models.DecimalField(max_digits=6, decimal_places=1,blank=False, verbose_name='Ποσό Εγγραφής')
    location = models.CharField(max_length=100,blank=False, verbose_name='Τοποθεσία')
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'Υπο Έλεγχο',
        verbose_name='Κατάσταση'
        )
    def __str__(self):
        # return '{self.id}_{self.title}'.format(self=self)
        return self.title
        
    class Meta:
        verbose_name = 'Αίτηση Μετακίνησης'
        verbose_name_plural = 'Αιτήσεις Μετακινήσεων'
