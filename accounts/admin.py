from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from accounts.models import Profile, Student
from student.models import *
# Register your models here.

class ProfileA(admin.ModelAdmin):
    
    list_display = ('user','department','title')



admin.site.register(Profile,ProfileA)
#admin.site.register(PaymentInstallment)
admin.site.register(Student)


admin.site.site_header = ' Hua Admin'
admin.site.site_title = 'Hua PostGrad Portal'


