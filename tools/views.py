from rest_framework.viewsets import ReadOnlyModelViewSet

from tools.models import Tools
from tools.serializers import ToolsSerializer


class ToolsReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer
    lookup_field = 'id'
