from django.urls import path

from orders.views import UserFeedbackCreateAPIView

urlpatterns = [
    path('user-feedback/', UserFeedbackCreateAPIView.as_view(), name='user_feedback-create'),
]
