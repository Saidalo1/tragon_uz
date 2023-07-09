from rest_framework.generics import ListAPIView

from tools.models import Tools
from tools.serializers import ToolsSerializer


class ToolsListAPIView(ListAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer
