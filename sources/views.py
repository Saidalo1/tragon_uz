from rest_framework.viewsets import ReadOnlyModelViewSet

from sources.serializers import SourceSerializer
from tools.models import Tools


class SourceReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Tools.objects.all()
    serializer_class = SourceSerializer
    lookup_field = 'id'
