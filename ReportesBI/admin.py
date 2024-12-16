from django.contrib import admin

import ReportesBI
from ReportesBI.models import ReportBi


# Register your models here.
@admin.register(ReportBi)
class ReportBiAdmin(admin.ModelAdmin):
    pass