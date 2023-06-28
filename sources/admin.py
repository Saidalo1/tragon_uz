from django.contrib import admin

from sources.models import Source


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    exclude = ()
