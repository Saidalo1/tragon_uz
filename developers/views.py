from rest_framework.viewsets import ReadOnlyModelViewSet

from developers.models import Developer
from developers.serializers import DeveloperSerializer


class DeveloperReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    lookup_field = 'id'
