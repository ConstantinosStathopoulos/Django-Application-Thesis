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

    # gets the data of user from ldap, adding department and title.
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.get_or_create(user=instance, department=instance.department, title=instance.title)
            
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        instance.profile.save()



class Student(models.Model):
    FULLTIME = 'FT'
    PARTTIME = 'PT'
    
    DURATION_CHOICES = [
        (FULLTIME, 'Full Time'),
        (PARTTIME, 'Part Time'),
    ] 

    # ? How to get only students
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True)
    postgrad_program = models.CharField(max_length=200, null=True)
    program_duration = models.CharField(max_length=2, choices=DURATION_CHOICES,default=FULLTIME)
