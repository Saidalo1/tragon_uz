from django.db.models import CharField, URLField, ImageField

from shared.django.models import CreatedTimeBaseModel


class Project(CreatedTimeBaseModel):
    title = CharField(max_length=100)
    link = URLField()
    photo = ImageField(upload_to='project_photos')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'project'
