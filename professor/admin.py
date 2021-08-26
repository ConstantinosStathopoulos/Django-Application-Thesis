from django.contrib import admin
from django.utils.html import format_html
from django.utils.html import strip_tags
from import_export.admin import ExportActionMixin, ImportExportMixin, ImportExportModelAdmin,ImportExportActionModelAdmin

# Register your models here.
from .models import FundingRequisition, SpeechRequisition, TravelRequisition
#Accept action
def set_status_accepted(modeladmin, request,queryset):
    queryset.update(status = 'Αποδεκτή')

#Action Description
set_status_accepted.short_description = "Αποδοχή επιλεγμένων αιτήσεων"


#Deny action
def set_status_denied(modeladmin, request,queryset):
    queryset.update(status = 'Μη Αποδεκτή')

#Action Description
set_status_denied.short_description = "Απόριψη επιλεγμένων αιτήσεων"






# classes representation in the admin page, they follow the same name as in models.py followed by A for Admin.
class SpeechRequisitionA(ImportExportMixin,admin.ModelAdmin):
    list_display = ('user', 'title', 'created_on', 'updated_on','requested_date' ,'description' ,'status')
    list_editable = ("status",)
    list_filter = ('user', 'requested_date','status', 'created_on')
    search_fields = ('user__username',)
    actions = [set_status_accepted, set_status_denied]

    

class FundingRequisitionA(ImportExportMixin, admin.ModelAdmin):
    list_display = ('user', 'title', 'created_on', 'updated_on','amount' ,'description' ,'status')
    list_editable = ("status",)
    list_filter = ('user', 'amount','status', 'created_on')
    search_fields = ('user__username',)
    actions = [set_status_accepted, set_status_denied]

    
    


    

class TravelRequisitionA(ImportExportMixin, admin.ModelAdmin):
    list_display = ('user', 'title', 'created_on', 'updated_on','requested_date' ,'description' ,'travel_fees' ,'accommodation_fees', 'registration_fees', 'location', 'status')
    list_editable = ("status",)
    list_filter = ('user', 'location','status', 'created_on')
    search_fields = ('user__username','location')
    actions = [set_status_accepted, set_status_denied]
    





#Registering models for admin page
admin.site.register(SpeechRequisition,SpeechRequisitionA)
admin.site.register(FundingRequisition,FundingRequisitionA)
admin.site.register(TravelRequisition,TravelRequisitionA)