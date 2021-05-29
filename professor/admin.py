from django.contrib import admin

# Register your models here.
from .models import FundingRequisition, SpeechRequisition
#Accept action
def set_status_accepted(modeladmin, request,queryset):
    queryset.update(status = 'Accepted')

#Action Description
set_status_accepted.short_description = "Accept Selected Requests"


#Deny action
def set_status_denied(modeladmin, request,queryset):
    queryset.update(status = 'Denied')

#Action Description
set_status_denied.short_description = "Deny Selected Requests"


class SpeechRequisitionA(admin.ModelAdmin):
    list_display = ('user', 'title', 'date','requested_date' ,'description' ,'status')
    list_editable = ("status",)
    list_filter = ('user', 'requested_date','status', 'date')
    search_fields = ('user__username',)
    actions = [set_status_accepted, set_status_denied]

class FundingRequisitionA(admin.ModelAdmin):
    list_display = ('user', 'title', 'date','amount' ,'description' ,'status')
    list_editable = ("status",)
    list_filter = ('user', 'amount','status', 'date')
    search_fields = ('user__username',)
    actions = [set_status_accepted, set_status_denied]



admin.site.register(SpeechRequisition,SpeechRequisitionA)
admin.site.register(FundingRequisition,FundingRequisitionA)
