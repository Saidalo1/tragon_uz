from rest_framework.viewsets import ReadOnlyModelViewSet

from tragon.models import Service
from tragon.serializers import ServiceSerializer


class ServiceReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'id'
