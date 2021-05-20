from django.db import models
from accounts.models import Profile
from datetime import datetime
from django.contrib.auth.models import User


STATUS_CHOICES = (
    ("Accepted", "Accepted"),
    ("Denied", "Denied"),
    ("Pending", "Pending")
)



class FundingRequisition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(blank=False)
    amount = models.DecimalField(max_digits=6, decimal_places=1)
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'Pending'
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
    requested_date = models.DateTimeField()
    description = models.TextField(blank=False)
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'Pending'
        )

    def __str__(self):
        return '{self.user}_{self.title}_{self.date}'.format(self=self)

    class Meta:
        verbose_name = 'Αίτηση Εκδήλωσης'
        verbose_name_plural = 'Αιτήσεις Εκδήλωσης'