from django.urls import path

from services.views import ServiceListAPIView

urlpatterns = [
    path('services/', ServiceListAPIView.as_view(), name='service-list'),
]
