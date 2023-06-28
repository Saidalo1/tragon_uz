from django.contrib import admin

from tools.models import Tools


@admin.register(Tools)
class ToolsAdmin(admin.ModelAdmin):
    exclude = ()
