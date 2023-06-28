from rest_framework.routers import DefaultRouter

from developers.views import DeveloperReadOnlyModelViewSet

router = DefaultRouter()
router.register('developers', DeveloperReadOnlyModelViewSet, 'developers')

urlpatterns = [
    *router.urls,
]
