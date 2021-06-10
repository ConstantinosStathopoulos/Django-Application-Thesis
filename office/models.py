from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

#Model for new announcements from the Office

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    text = RichTextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ανακοίνωση" 
        verbose_name_plural = "Ανακοινώσεις"
