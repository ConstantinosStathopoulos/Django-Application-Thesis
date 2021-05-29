from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


#creates a proxy model, based on auth_user, extending it for more information
class Profile(models.Model):
    # primary_key=True
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100,  null=True, blank=True)
## ? Should I create is_student, is_professor, is_office booleans to keep track of users?
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Προφίλ Χρηστών'
        


class Student(models.Model):

    MAJOR_OPTIONS = [
        ("Κατεύθυνση 1η: Τεχνολογίες και Εφαρμογές Ιστού", "Κατεύθυνση 1η: Τεχνολογίες και Εφαρμογές Ιστού"),
        ("Κατεύθυνση 2η: Διαχείριση Δικτύων Επικοινωνιών και Υπηρεσιών Επόμενης Γενιάς", "Κατεύθυνση 2η: Διαχείριση Δικτύων Επικοινωνιών και Υπηρεσιών Επόμενης Γενιάς"),
        ("Κατεύθυνση 3η: Πληροφοριακά Συστήματα στη Διοίκηση Επιχειρήσεων", "Κατεύθυνση 3η: Πληροφοριακά Συστήματα στη Διοίκηση Επιχειρήσεων")
    ]


    DURATION_CHOICES = [
        ("Πλήρης Φοίτηση", "Πλήρης Φοίτηση"),
        ("Μερική Φοίτηση", "Μερική Φοίτηση")
    ] 

    # ? How to get only students
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True)
    postgrad_program = models.CharField(max_length=80,choices=MAJOR_OPTIONS, null=True)
    program_duration = models.CharField(max_length=14, choices=DURATION_CHOICES, null=True)

    def __str__(self):
        return '{self.profile.user.username}'.format(self=self) 
        


    class Meta:
        verbose_name = 'Φοιτητής'
        verbose_name_plural = 'Φοιτητές'