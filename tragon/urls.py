# urls.py
from rest_framework import routers

from tragon.views import ServiceReadOnlyModelViewSet

router = routers.DefaultRouter()
router.register('services', ServiceReadOnlyModelViewSet)

urlpatterns = [
    *router.urls,
]
