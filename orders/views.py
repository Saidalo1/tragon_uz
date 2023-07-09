from rest_framework.generics import CreateAPIView

from orders.serializers import UserFeedbackSerializer


class UserFeedbackCreateAPIView(CreateAPIView):
    serializer_class = UserFeedbackSerializer

