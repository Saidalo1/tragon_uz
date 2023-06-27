from django.urls import path
from rest_framework import routers

from tragon.views import (
    ServiceReadOnlyModelViewSet, SubServiceAPIView,
    DeveloperReadOnlyModelViewSet, ProjectReadOnlyModelViewSet, ToolsReadOnlyModelViewSet,
    UserFeedbackCreateAPIView, SourceReadOnlyModelViewSet
)

router = routers.DefaultRouter()
router.register('services', ServiceReadOnlyModelViewSet)
router.register('sources', SourceReadOnlyModelViewSet)
router.register('developers', DeveloperReadOnlyModelViewSet)
router.register('projects', ProjectReadOnlyModelViewSet)
router.register('tools', ToolsReadOnlyModelViewSet)

urlpatterns = [
    *router.urls,
    path('services-price/', SubServiceAPIView.as_view(), name='service_price-list'),
    path('user-feedback/', UserFeedbackCreateAPIView.as_view(), name='user_feedback-create'),
]
