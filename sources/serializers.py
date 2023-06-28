from rest_framework.serializers import ModelSerializer

from sources.models import Source


class SourceSerializer(ModelSerializer):
    class Meta:
        model = Source
        exclude = ('created_at', 'updated_at')
