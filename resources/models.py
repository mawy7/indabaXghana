from django.conf import settings
from django.db import models
from django.utils import timezone

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django_extensions.db.fields import AutoSlugField
from django_slugify_processor.text import slugify
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.encoding import python_2_unicode_compatible

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

@python_2_unicode_compatible
 
class Slide(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slide_src = models.CharField(max_length=200,default="")
    slide_url = models.CharField(max_length=200, default='', help_text='Link to Slide', blank=True,)
    slide_title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slide_title

 
class Photo(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    indabax_edition = models.CharField(max_length=200, null=True, blank=True,)
    photo = ProcessedImageField(upload_to='static/photos/',default="team.png", processors=[ResizeToFit(1000)], format='jpeg', options={'quality': 90})
    photo_description = models.TextField(default=" ", null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.indabax_edition


class Video(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=200)
    video_youtube_url = models.URLField(default='', help_text='Link to Video')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_title
