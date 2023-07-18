from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from orders.forms import UserFeedbackForm
from orders.models import UserFeedback, UserFeedbackService
from shared.django.utils import send_notification


@admin.register(UserFeedback)
class UserFeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'get_ordered_services', 'source', 'created_at', 'total_price')
    form = UserFeedbackForm

    def get_ordered_services(self, obj):
        services = obj.services.all()
        service_links = []
        for service in services:
            service_link = reverse('admin:services_subservice_change', args=[service.pk])
            service_link_html = format_html('<a href="{}">{}</a>', service_link, service.name)
            service_links.append(service_link_html)
        return format_html(', '.join(service_links))

    get_ordered_services.short_description = 'Ordered Services'

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        selected_services = form.cleaned_data.get('services')

        if selected_services:
            feedback = form.instance
            try:
                UserFeedback.objects.get(name=feedback.name, source=feedback.source, phone=feedback.phone,
                                         created_at=feedback.created_at)
            except UserFeedback.DoesNotExist:
                feedback_services = [UserFeedbackService(feedback=feedback, service=service) for service in
                                     selected_services]
                UserFeedbackService.objects.bulk_create(feedback_services)

                send_notification().delay(feedback.name, feedback.phone, str(feedback.source),
                                          [str(service) for service in selected_services], feedback.total_price)
