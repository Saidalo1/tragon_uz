from django.db.models import ForeignKey, CASCADE, CharField, ManyToManyField, Sum

from services.models import SubService
from shared.django.models import CreatedTimeBaseModel
from sources.models import Source


class UserFeedbackService(CreatedTimeBaseModel):
    feedback = ForeignKey('UserFeedback', CASCADE, related_name='user_feedback_services', db_index=True)
    service = ForeignKey(SubService, CASCADE)

    class Meta:
        db_table = 'user_feedback_services'


class UserFeedback(CreatedTimeBaseModel):
    name = CharField(max_length=255)
    phone = CharField(max_length=20)
    source = ForeignKey(Source, CASCADE)
    services = ManyToManyField(SubService, through=UserFeedbackService, related_name='feedbacks')

    @property
    def total_price(self):
        return f"{self.services.aggregate(total=Sum('price'))['total'] or 0}$"

    class Meta:
        db_table = 'user_feedback'
