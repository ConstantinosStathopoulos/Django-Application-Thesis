
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Student
from django.core.mail import send_mail






@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance, department=instance.department, title=instance.title)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    instance.profile.save()



#signal to create student if the profile created contains "μεταπτυχιακος φοιτητης"
@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):

    if created == False:
        if instance.profile.title == 'Μεταπτυχιακός Φοιτητής':
            Student.objects.get_or_create(profile=instance.profile)
            print('Student Created!')
            #here the signal will send an email to the office, to inform that a new student has been created, and that the record needs attention.
            # subject = 'Είσοδος Νέου Φοιτητή στο σύστημα Μεταπτυχιακού'
            # message = 'Ένας νέος φοιτητής συνδέθηκε στο σύστημα διαχείρησης Μεταπτυχιακού Προγράμματος Σπουδών. Παρακαλώ εισέλθετε στην εφαρμογή για να ορίσετε το πρόγραμμα σπουδών του.'

            # send_mail(
            #     subject,
            #     message,
            #     'it214100@hua.gr',
            #     ['constantinos.stath@gmail.com'],
            #     fail_silently=False,
            # )


