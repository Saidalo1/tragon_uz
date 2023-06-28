from rest_framework.serializers import ModelSerializer

from tools.models import Tools


class ToolsSerializer(ModelSerializer):
    class Meta:
        model = Tools
        exclude = ('created_at', 'updated_at')
