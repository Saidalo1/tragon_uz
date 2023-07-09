from django.contrib import admin

from tools.models import Tools, SubTools


@admin.register(Tools)
class ToolsAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(SubTools)
class SubToolsAdmin(admin.ModelAdmin):
    exclude = ()
