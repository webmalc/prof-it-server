from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from unidecode import unidecode


class SlugModel(models.Model):
    """ Slug mixin """

    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id or not self.slug:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class KeywordsDescModel(models.Model):
    """ KeywordsDescModel mixin """

    keywords = models.CharField(
        max_length=255, db_index=True, verbose_name=_('keywords'))
    meta_description = models.CharField(
        max_length=255, db_index=True, verbose_name=_('meta_description'))

    class Meta:
        abstract = True
