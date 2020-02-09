from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime
from datetime import date



# Create your models here.


class Sponsor(models.Model):
    created_date = models.DateField(default=date.today, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sponsor_image = models.ImageField(upload_to='sponsor/',default="sponsor.png")
    organization = models.CharField(max_length=50, null=True, help_text="What is the name of the Organization")
    website_url = models.URLField(default='', help_text='Link to Event Website', blank=True,)
    
    
    def __str__(self):
        return self.organization