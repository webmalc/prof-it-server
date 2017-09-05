from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel
from ordered_model.models import OrderedModel

from profit.models import MetaModel, SlugModel


class Technology(TimeStampedModel, TitleDescriptionModel, SlugModel):
    """ Technology class """
    works = models.ManyToManyField(
        'Work', verbose_name=_('works'), related_name='works')

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = 'modified'
        ordering = ('title', )
        verbose_name_plural = "technologies"


class Work(TimeStampedModel, TitleDescriptionModel, OrderedModel, MetaModel):
    """ Work class """

    content = models.TextField(_('content'), db_index=True)
    technologies = models.ManyToManyField(
        'Technology',
        through=Technology.works.through,
        verbose_name=_('technologies'),
        related_name='technologies')

    class Meta(OrderedModel.Meta):
        pass
