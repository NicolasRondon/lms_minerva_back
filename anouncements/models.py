from django.db import models

# Create your models here.
class Anouncement(models.Model):
    title = models.CharField(max_length=250, blank=False)
    body= models.TextField(blank=False)
    date_created = models.DateFieldTime(auto_now_add=True)
    date_update = models.DateFieldTime(auto_now=True)

    def __str__(self):
        return self.title


