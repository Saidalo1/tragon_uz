from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from orders.models import UserFeedback
from services.models import SubService


class UserFeedbackSerializer(ModelSerializer):
    services = PrimaryKeyRelatedField(queryset=SubService.objects.all(), many=True)

    class Meta:
        model = UserFeedback
        fields = ('name', 'phone', 'source', 'services')

    def create(self, validated_data):
        services_data = validated_data.pop('services')
        user_feedback, created = UserFeedback.objects.get_or_create(**validated_data)
        for service_data in services_data:
            service = SubService.objects.get(pk=service_data.pk)
            user_feedback.services.add(service)
        return user_feedback
