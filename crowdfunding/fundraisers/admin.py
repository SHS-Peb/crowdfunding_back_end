from django.contrib import admin
from .models import Fundraiser

@admin.register(Fundraiser)
class FundraiserAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "status", "is_open", "date_created")
    list_filter = ("status", "is_open")
    readonly_fields = ("owner", "date_created")
