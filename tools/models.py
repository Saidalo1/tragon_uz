from django.db.models import CharField, ForeignKey, CASCADE

from shared.django.models import CreatedTimeBaseModel


class Tools(CreatedTimeBaseModel):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tools'
        verbose_name_plural = 'Tools'


class SubTools(CreatedTimeBaseModel):
    name = CharField(max_length=255)
    tools = ForeignKey(Tools, CASCADE, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sub_tools'
        verbose_name_plural = 'Sub Tools'
