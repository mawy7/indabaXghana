from django.contrib import admin

# Register your models here.

from .models import SpeakerSchedule, Event, Day

admin.site.register(SpeakerSchedule)
admin.site.register(Event)
admin.site.register(Day)