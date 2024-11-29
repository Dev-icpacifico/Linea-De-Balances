from django.contrib import admin

import ReportesBI
from ReportesBI.models import EmptyModel


# Register your models here.
@admin.register(EmptyModel)
class EmptyModelAdmin(admin.ModelAdmin):
    pass
