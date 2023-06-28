from rest_framework.generics import CreateAPIView

from orders.models import UserFeedback
from orders.serializers import UserFeedbackSerializer


class UserFeedbackCreateAPIView(CreateAPIView):
    serializer_class = UserFeedbackSerializer
    queryset = UserFeedback.objects.all()
