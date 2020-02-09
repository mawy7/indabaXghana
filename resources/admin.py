from django.contrib import admin
from .models import Slide, Photo, Video
# Register your models here.


class SlideAdmin(admin.ModelAdmin):
    list_display = ("slide_title","created_at")
    list_filter = ("slide_title","created_at")


class PhotoAdmin(admin.ModelAdmin):
    list_display = ("indabax_edition","created_at")
    list_filter = ("indabax_edition","created_at")


class VideoAdmin(admin.ModelAdmin):
    list_display = ("video_title","created_at")
    list_filter = ("video_title","created_at")


admin.site.register(Slide, SlideAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video, VideoAdmin)
