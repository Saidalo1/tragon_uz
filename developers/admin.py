from django.contrib import admin

from developers.models import Developer


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    exclude = ()
