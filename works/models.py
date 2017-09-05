from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel
from ordered_model.models import OrderedModel

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToCover, Thumbnail
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


class Photo(TitleDescriptionModel, OrderedModel):
    """
    Photo class
    """
    is_default = models.BooleanField(
        default=False, verbose_name=_('is default?'))
    photo = ProcessedImageField(
        upload_to='works_photos',
        processors=[ResizeToCover(600, 600, False)],
        format='JPEG',
        options={'quality': 90},
        verbose_name=_('photo'))
    thumbnail = ImageSpecField(
        source='photo',
        processors=[Thumbnail(120, 120)],
        format='JPEG',
        options={'quality': 90})

    thumbnail_xs = ImageSpecField(
        source='photo',
        processors=[Thumbnail(30, 30)],
        format='JPEG',
        options={'quality': 90})

    preview_photo = ImageSpecField(
        source='photo',
        processors=[ResizeToCover(300, 300, False)],
        format='JPEG',
        options={'quality': 90})

    work = models.ForeignKey(
        Work, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return self.title if self.title else 'photo #{}'.format(self.id)

    def photo_tag(self):
        return mark_safe("""<a href="{}" target="_blank">
            <img src="{}" width="{}" height="{}" />
            </a>""".format(self.photo.url, self.thumbnail_xs.url,
                           self.thumbnail_xs.width, self.thumbnail_xs.height))

    photo_tag.short_description = 'Preview'

    class Meta:
        ordering = ['-is_default']
