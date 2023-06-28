from django.db.models import CharField

from shared.django.models import CreatedTimeBaseModel


class Source(CreatedTimeBaseModel):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'source'
