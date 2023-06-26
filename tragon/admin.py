from django.contrib import admin
from django.contrib.admin import ModelAdmin

from tragon.models import Service


# Register your models here.

@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    exclude = ()
