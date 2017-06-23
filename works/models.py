from django_extensions.db.models import (TimeStampedModel,
                                         TitleSlugDescriptionModel)


class Technology(TimeStampedModel, TitleSlugDescriptionModel):
    """ Technology class """

    class Meta:
        get_latest_by = 'modified'
        ordering = ('title', )
