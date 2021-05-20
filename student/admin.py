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
    list_display = ('user', 'installment', 'date','document' , 'status')
    list_editable = ("status",)
    list_filter = ('user', 'installment','status', 'date')
    search_fields = ('user__username',)
    actions = [set_status_accepted, set_status_denied]

class PaymentInstallmentA(admin.ModelAdmin):
    list_display = ('name','due_date','amount')
    list_filter = ('name','due_date','amount')


admin.site.register(Payment,PaymentA)
admin.site.register(PaymentInstallment,PaymentInstallmentA)