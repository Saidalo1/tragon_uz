from rest_framework.serializers import ModelSerializer

from portfolios.models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        exclude = ('created_at', 'updated_at')
