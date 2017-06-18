from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from unidecode import unidecode


class ExtendedFlatPage(FlatPage):
    """
    Page class
    """
    slug = models.SlugField()
    keywords = models.CharField(max_length=255, verbose_name=_('keywords'))
    description = models.CharField(
        max_length=255, verbose_name=_('description'))

    def save(self, *args, **kwargs):
        if not self.id or not self.slug:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)
