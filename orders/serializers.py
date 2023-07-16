from rest_framework.exceptions import ValidationError
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from orders.models import UserFeedback, UserFeedbackService
from services.models import SubService
from shared.django.functions import validate_phone_number
from shared.django.utils import send_notification
from sources.models import Source


class UserFeedbackSerializer(ModelSerializer):
    services = PrimaryKeyRelatedField(queryset=SubService.objects.all(), many=True)

    class Meta:
        model = UserFeedback
        fields = ('name', 'phone', 'source', 'services')

    @staticmethod
    def validate_phone(value):
        try:
            validate_phone_number(value)
        except ValidationError:
            raise ValidationError(
                'Invalid phone number. Please, provide a valid phone number in the format of Uzbekistan.')
        return value

    @staticmethod
    def validate_source(value):
        if not Source.objects.filter(id=value.id).exists():
            raise ValidationError('Invalid source. Please provide a valid source ID.')
        return value

    @staticmethod
    def validate_services(value):
        if not value:
            raise ValidationError('At least one service ID must be provided.')
        return value

    def create(self, validated_data):
        services_data = validated_data.pop('services')
        user_feedback = UserFeedback.objects.create(**validated_data)
        feedback_services = [UserFeedbackService(feedback=user_feedback, service_id=service_data.pk) for service_data in
                             services_data]
        UserFeedbackService.objects.bulk_create(feedback_services)

        services_data_str = [str(service) for service in services_data]

        send_notification.delay(user_feedback.name, user_feedback.phone, str(user_feedback.source), services_data_str)
        return user_feedback
