from django.contrib import admin

from services.models import Service, SubService


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(SubService)
class SubServiceAdmin(admin.ModelAdmin):
    exclude = ()
