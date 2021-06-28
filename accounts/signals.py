
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Student
from django.core.mail import send_mail
from django.conf import settings






@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance, department=instance.department, title=instance.title)
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    instance.profile.save()
    #check if it is a postgrad student
    if instance.profile.title == 'Μεταπτυχιακός Φοιτητής':
        #if its the first time to login, create a student profile and alert office.
        if instance.profile.user.last_login == None :
            Student.objects.get_or_create(profile=instance.profile)
            print('Student Created!')
            #here the signal will send an email to the office, to inform that a new student has been created, and that the record needs attention.
            subject = 'Είσοδος Νέου Φοιτητή στο σύστημα Μεταπτυχιακού Προγράμματος Σπουδών.'
            message = 'Ένας νέος χρήστης (' + instance.profile.user.username +') με την ιδιότητα του Μεταπτυχιακού φοιτητή συνδέθηκε στο σύστημα διαχείρησης Μεταπτυχιακού Προγράμματος Σπουδών. Παρακαλώ εισέλθετε στην εφαρμογή για να ορίσετε το πρόγραμμα σπουδών του.'

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                ['it214100@hua.gr'],
                fail_silently=False,
            )


