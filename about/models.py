import datetime
from datetime import date
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django_extensions.db.fields import AutoSlugField
from django_slugify_processor.text import slugify
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.encoding import python_2_unicode_compatible
@python_2_unicode_compatible
 
 

# Create your models here.
 
class About(models.Model):
    created_date = models.DateField(default=date.today, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    display_image = models.ImageField(upload_to='team/',default="team.png")
    member_name = models.CharField(max_length=50, help_text="What is the name of team member")
    member_twitter = models.CharField(max_length=100, null=True, help_text="Please enter only the user name eg.'mawy_7' ", default=" ")
    member_linkedin = models.CharField(max_length=100, null=True, help_text="Please enter only the user name eg. in/mawy7 ", default=" ")
    dispaly_member = models.BooleanField(default=False)
    slug = AutoSlugField(
        populate_from='member_name',
        slugify_function=slugify
    )

    def __str__(self):
        return self.member_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.member_name)
        return super(About, self).save(*args, **kwargs)
