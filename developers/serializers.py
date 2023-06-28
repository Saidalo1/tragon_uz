from rest_framework.serializers import ModelSerializer

from developers.models import Developer


class DeveloperSerializer(ModelSerializer):
    class Meta:
        model = Developer
        exclude = ('created_at', 'updated_at')
