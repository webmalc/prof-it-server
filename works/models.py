from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel

from profit.models import SlugModel


class Technology(TimeStampedModel, TitleDescriptionModel, SlugModel):
    """ Technology class """

    class Meta:
        get_latest_by = 'modified'
        ordering = ('title', )
        verbose_name_plural = "technologies"
