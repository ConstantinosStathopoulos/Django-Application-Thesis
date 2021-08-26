from django.contrib import admin
from .models import Payment, PaymentInstallment
from import_export.admin import ImportExportMixin, ImportExportActionModelAdmin
# Register your models here.

# Admin Action Functions

# accept payment
def set_status_accepted(modeladmin, request,queryset):
    queryset.update(status = 'Αποδεκτή')

#Action Description
set_status_accepted.short_description = "Αποδοχή επιλεγμένων Πληρωμών"

#deny payment
def set_status_denied(modeladmin, request,queryset):
    queryset.update(status = 'Μη Αποδεκτή')

set_status_denied.short_description = "Απόριψη επιλεγμένων Πληρωμών"

class PaymentA(ImportExportMixin, admin.ModelAdmin):
    list_display = ('student', 'installment', 'created_on','updated_on','document' , 'status')
    list_editable = ("status",)
    list_filter = ('student', 'installment','status', 'created_on', 'updated_on')
    search_fields = ('student.profile.user__username',)
    actions = [set_status_accepted, set_status_denied]



class PaymentInstallmentA(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('name','due_date','program_duration','postgrad_year', 'amount')
    list_filter = ('name','program_duration','postgrad_year')
    list_editable = ("amount","due_date","postgrad_year")


admin.site.register(Payment,PaymentA)
admin.site.register(PaymentInstallment,PaymentInstallmentA)