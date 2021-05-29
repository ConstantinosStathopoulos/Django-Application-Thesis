from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from accounts.models import Profile, Student
from student.models import *
# Register your models here.


admin.site.site_header = ' Πλατφόρμα Διαχείρησης Μεταπτυχιακού Προγράμματος Χαροκοπείου'
admin.site.site_title = 'Hua PostGrad Portal'

class ProfileA(admin.ModelAdmin):
    list_display = ('user','department','title')
    list_filter = ('department', 'title')
    search_fields = ('user__username',)


class StudentA(admin.ModelAdmin):
    list_display = ('profile','postgrad_program','program_duration')
    list_filter = ('postgrad_program', 'program_duration')
    search_fields = ('profile__user__username',)
    list_editable = ('postgrad_program', 'program_duration')

admin.site.register(Profile,ProfileA)
#admin.site.register(PaymentInstallment)
admin.site.register(Student,StudentA)



