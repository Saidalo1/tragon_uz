from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from tragon.models import Service, SubService, UserFeedback, Developer, Project, Tools
from tragon.serializers import ServiceSerializer, SubServiceSerializer, UserFeedbackSerializer, DeveloperSerializer, \
    ProjectSerializer, ToolsSerializer, SourceSerializer


class ServiceReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'id'


class SubServiceAPIView(GenericAPIView):
    queryset = SubService.objects.all()
    serializer_class = SubServiceSerializer

    @staticmethod
    def get(request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


class UserFeedbackCreateAPIView(CreateAPIView):
    serializer_class = UserFeedbackSerializer
    queryset = UserFeedback.objects.all()


class DeveloperReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    lookup_field = 'id'


class ProjectReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'


class ToolsReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer
    lookup_field = 'id'


class SourceReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Tools.objects.all()
    serializer_class = SourceSerializer
    lookup_field = 'id'
