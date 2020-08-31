from django.db import models
from accounts.models import MinervaUser
# Create your models here.
class Anouncement(models.Model):
    title = models.CharField(max_length=250, blank=False)
    body= models.TextField(blank=False)
    date_created = models.DateFieldTime(auto_now_add=True)
    date_update = models.DateFieldTime(auto_now=True)
    users = models.ManyToManyField(MinervaUser)

    def __str__(self):
        return self.title


