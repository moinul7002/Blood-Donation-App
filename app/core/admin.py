from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

@admin.register(Donor)
class DonorAdmin(ImportExportModelAdmin):
    list_display = ['firstname','lastname','age','sex','location','blood_group']