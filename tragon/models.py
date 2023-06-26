from ckeditor.fields import RichTextField
from django.db.models import CharField, Model


class Service(Model):
    name = CharField(max_length=100)
    description = RichTextField()

    def __str__(self):
        return self.name
