from rest_framework.routers import DefaultRouter

from tools.views import ToolsReadOnlyModelViewSet

router = DefaultRouter()
router.register('tools', ToolsReadOnlyModelViewSet, 'tools')

urlpatterns = [
    *router.urls
]
