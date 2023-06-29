from django.db.models import CharField, CASCADE
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from shared.django.models import CreatedTimeBaseModel


class Tools(MPTTModel, CreatedTimeBaseModel):
    name = CharField(max_length=100)
    parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        db_table = 'tools'

    def __str__(self):
        return self.name
