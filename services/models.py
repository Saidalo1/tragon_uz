from ckeditor.fields import RichTextField
from django.db.models import CharField, DecimalField, ForeignKey, CASCADE

from shared.django.models import CreatedTimeBaseModel


class Service(CreatedTimeBaseModel):
    name = CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'services'


class SubService(CreatedTimeBaseModel):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=8, decimal_places=2)
    service = ForeignKey(Service, CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sub_service'
