from rest_framework.viewsets import ReadOnlyModelViewSet

from portfolios.models import Project
from portfolios.serializers import ProjectSerializer


class ProjectReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'
