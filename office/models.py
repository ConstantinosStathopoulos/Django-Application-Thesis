from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

#Model for new announcements from the Office

class Announcement(models.Model):
    title = models.CharField(max_length=100, verbose_name='Τίτλος')
    text = RichTextField(verbose_name='Κείμενο')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Ημερομηνία')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ανακοίνωση" 
        verbose_name_plural = "Ανακοινώσεις"
