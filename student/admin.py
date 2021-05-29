from django.contrib import admin
from .models import Payment, PaymentInstallment
# Register your models here.

# Admin Action Functions

# accept payment
def set_status_accepted(modeladmin, request,queryset):
    queryset.update(status = 'Accepted')

#Action Description
set_status_accepted.short_description = "Αποδοχή επιλεγμένων Πληρωμών"

#deny payment
def set_status_denied(modeladmin, request,queryset):
    queryset.update(status = 'Denied')

set_status_denied.short_description = "Απόριψη επιλεγμένων Πληρωμών"

class PaymentA(admin.ModelAdmin):
    list_display = ('student', 'installment', 'date','document' , 'status')
    list_editable = ("status",)
    list_filter = ('student', 'installment','status', 'date')
    search_fields = ('student.profile.user__username',)
    actions = [set_status_accepted, set_status_denied]

class PaymentInstallmentA(admin.ModelAdmin):
    list_display = ('name','due_date','program_duration', 'amount')
    list_filter = ('name','program_duration')
    list_editable = ("amount","due_date")


admin.site.register(Payment,PaymentA)
admin.site.register(PaymentInstallment,PaymentInstallmentA)