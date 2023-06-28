from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from orders.models import UserFeedback


@admin.register(UserFeedback)
class UserFeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'get_ordered_services',  'source', 'created_at')

    def get_ordered_services(self, obj):
        services = obj.services.all()
        service_links = []
        for service in services:
            service_link = reverse('admin:services_subservice_change', args=[service.pk])
            service_link_html = format_html('<a href="{}">{}</a>', service_link, service.name)
            service_links.append(service_link_html)
        return format_html(', '.join(service_links))

    get_ordered_services.short_description = 'Ordered Services'
