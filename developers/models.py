from django.db.models import CharField, ImageField

from shared.django.models import CreatedTimeBaseModel


class Developer(CreatedTimeBaseModel):
    name = CharField(max_length=255)
    profile_photo = ImageField(upload_to='profile_photos/')
    profession = CharField(max_length=255)

    class Meta:
        db_table = 'developer'
