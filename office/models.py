from django.db import models
from datetime import datetime

#Model for new announcements from the Office

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name:'Ανακοίνωση'
        verbose_name_plural:'Ανακοινώσεις'
