from  django.contrib import admin
from  .models import Speaker

admin.site.register(Speaker)

class SpeakerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('speaker_name',)}