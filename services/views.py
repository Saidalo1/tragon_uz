from rest_framework.generics import ListAPIView

from services.models import Service
from services.serializers import ServiceSerializer


class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
