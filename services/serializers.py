from rest_framework.serializers import ModelSerializer

from services.models import Service, SubService


class SubServiceSerializer(ModelSerializer):
    class Meta:
        model = SubService
        fields = ('id', 'name', 'price')


class ServiceSerializer(ModelSerializer):
    sub_services = SubServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ('id', 'name', 'description', 'sub_services')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['sub_services'] = SubServiceSerializer(instance.subservice_set.all(), many=True).data
        return representation
