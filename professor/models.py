from django.db import models
from accounts.models import Profile
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

STATUS_CHOICES = (
    ("Αποδεκτή", "Αποδεκτή"),
    ("Μη Αποδεκτή", "Μη Αποδεκτή"),
    ("Υπο Έλεγχο", "Υπο Έλεγχο")
)



class FundingRequisition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    description = RichTextField(blank=False)
    amount = models.DecimalField(max_digits=6, decimal_places=1)
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'Υπο Έλεγχο'
        )

    def __str__(self):
        return '{self.user}_{self.title}_{self.date}'.format(self=self)

    class Meta:
        verbose_name = 'Αίτηση Χρηματοδότησης'
        verbose_name_plural = 'Αιτήσεις Χρηματοδότησης'





class SpeechRequisition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    requested_date = models.DateField(verbose_name="Αιτούμενη Ημερομηνία", help_text="Εισάγετε την Ημερομηνία της Ομιλίας/Εκδήλωσης")
    requested_time = models.TimeField(verbose_name="Αιτούμενη Ώρα", help_text="Εισάγετε την Ώρα της Ομιλίας/Εκδήλωσης")
    description = RichTextField(blank=False)
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'Υπο Έλεγχο'
        )

    def __str__(self):
        return '{self.user}_{self.title}_{self.date}'.format(self=self)

    class Meta:
        verbose_name = 'Αίτηση Εκδήλωσης'
        verbose_name_plural = 'Αιτήσεις Εκδήλωσης'



class TravelRequisition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    requested_date = models.DateField()
    description = RichTextField(blank=False)
    travel_fees = models.DecimalField(max_digits=6, decimal_places=1, blank=False)
    accommodation_fees = models.DecimalField(max_digits=6, decimal_places=1,blank=False)
    registration_fees = models.DecimalField(max_digits=6, decimal_places=1,blank=False)
    location = models.CharField(max_length=100,blank=False)
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'Υπο Έλεγχο'
        )
    
    class Meta:
        verbose_name = 'Αίτηση Μετακίνησης'
        verbose_name_plural = 'Αιτήσεις Μετακινήσεων'
