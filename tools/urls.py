from django.urls import path

from tools.views import ToolsListAPIView

urlpatterns = [
    path('tools/', ToolsListAPIView.as_view(), name='tools')
]
