from django.db.models import CharField

from shared.django.models import CreatedTimeBaseModel


class Source(CreatedTimeBaseModel):
    name = CharField(max_length=255)

    class Meta:
        db_table = 'source'
