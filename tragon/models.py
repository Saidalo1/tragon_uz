from ckeditor.fields import RichTextField
from django.db.models import CharField, ImageField, URLField, CASCADE, DecimalField, ForeignKey, ManyToManyField
from mptt.models import TreeForeignKey, MPTTModel

from shared.django.models import CreatedTimeBaseModel


class Service(CreatedTimeBaseModel):
    name = CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'service'


class Developer(CreatedTimeBaseModel):
    name = CharField(max_length=255)
    profile_photo = ImageField(upload_to='profile_photos/')
    profession = CharField(max_length=255)

    class Meta:
        db_table = 'developer'


class Project(CreatedTimeBaseModel):
    title = CharField(max_length=100)
    link = URLField()
    photo = ImageField(upload_to='project_photos')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'project'


class Tools(MPTTModel, CreatedTimeBaseModel):
    name = CharField(max_length=100)
    parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        db_table = 'tools'


class SubService(CreatedTimeBaseModel):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=8, decimal_places=2)
    service = ForeignKey(Service, CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sub_service'


class Source(CreatedTimeBaseModel):
    name = CharField(max_length=255)

    class Meta:
        db_table = 'source'


class UserFeedback(CreatedTimeBaseModel):
    name = CharField(max_length=255)
    phone = CharField(max_length=20)
    source = ForeignKey(Source, CASCADE)
    services = ManyToManyField(SubService, related_name='feedbacks')

    class Meta:
        db_table = 'user_feedback'
