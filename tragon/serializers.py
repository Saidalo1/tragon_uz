from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from tragon.models import Service, SubService, UserFeedback, Developer, Project, Tools


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        exclude = ('created_at', 'updated_at')


class SourceSerializer(ModelSerializer):
    class Meta:
        model = Service
        exclude = ('created_at', 'updated_at')


class SubServiceSerializer(ModelSerializer):
    class Meta:
        model = SubService
        fields = ('name', 'price')


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


class DeveloperSerializer(ModelSerializer):
    class Meta:
        model = Developer
        exclude = ('created_at', 'updated_at')


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        exclude = ('created_at', 'updated_at')


class ToolsSerializer(ModelSerializer):
    class Meta:
        model = Tools
        exclude = ('created_at', 'updated_at')
