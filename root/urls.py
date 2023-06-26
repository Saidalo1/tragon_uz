from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Tragon API Documentation",
        default_version="v1",
        description="API documentation for Tragon",
    ),
    public=True,
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # index
    path('', include('tragon.urls')),

    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
