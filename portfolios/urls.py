from rest_framework.routers import DefaultRouter

from portfolios.views import ProjectReadOnlyModelViewSet

router = DefaultRouter()
router.register('projects', ProjectReadOnlyModelViewSet, 'projects')

urlpatterns = [
    *router.urls,
]
