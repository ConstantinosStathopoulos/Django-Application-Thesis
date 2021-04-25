from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from accounts.models import Profile, Student
from student.models import *
# Register your models here.

admin.site.register(Profile)
admin.site.register(PaymentInstallment)
admin.site.register(Student)
admin.site.register(Payment)


admin.site.site_header = ' Hua Admin'
admin.site.site_title = 'Hua PostGrad Portal'