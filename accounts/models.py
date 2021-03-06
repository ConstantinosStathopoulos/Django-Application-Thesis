from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


#creates a proxy model, based on auth_user, extending it for more information
class Profile(models.Model):
    # primary_key=True
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name='Χρήστη')
    department = models.CharField(max_length=100, null=True, blank=True, verbose_name='Τμήμα')
    title = models.CharField(max_length=100,  null=True, blank=True, verbose_name='Τίτλος')
## ? Should I create is_student, is_professor, is_office booleans to keep track of users?
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name='Προφίλ Χρήστη'
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

    YEAR_CHOICES = [
        (r,r) for r in range(2006, datetime.date.today().year+1)
    ]


    # ? How to get only students
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True, verbose_name='Προφίλ')
    postgrad_program = models.CharField(max_length=80,choices=MAJOR_OPTIONS, null=True, verbose_name='Μεταπτυχιακό Πρόγραμμα')
    program_duration = models.CharField(max_length=14, choices=DURATION_CHOICES, null=True, verbose_name='Διάρκεια Σπουδών')
    postgrad_year =  models.IntegerField(choices=YEAR_CHOICES, blank=True, null=True, default=datetime.datetime.now().year, verbose_name='Έτος Εγγραφής')

    def __str__(self):
        return '{self.profile.user.username}'.format(self=self) 
        

    

    class Meta:
        verbose_name = 'Φοιτητής'
        verbose_name_plural = 'Φοιτητές'