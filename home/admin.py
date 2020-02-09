from django.contrib import admin
from .models import Sponsor


admin.site.register(Sponsor)

class SponsorAdmin(admin.ModelAdmin):
    list_display = ("organization")
    list_filter = ("organization")
