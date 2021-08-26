from django.contrib import admin
from import_export.admin import ImportExportMixin

# Register your models here.
from .models import Announcement


class AnnouncementAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('title', 'date')
    



admin.site.register(Announcement,AnnouncementAdmin)