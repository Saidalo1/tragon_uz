from django.urls import path

from orders.views import UserFeedbackCreateAPIView

urlpatterns = [
    path('orders/', UserFeedbackCreateAPIView.as_view(), name='orders-create'),
]
