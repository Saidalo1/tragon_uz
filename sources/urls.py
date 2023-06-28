from rest_framework.routers import DefaultRouter

from sources.views import SourceReadOnlyModelViewSet

router = DefaultRouter()
router.register('sources', SourceReadOnlyModelViewSet, 'sources')

urlpatterns = [
    *router.urls
]
