from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.utils.translation import ugettext_lazy as _

from profit.models import SlugModel


class ExtendedFlatPage(FlatPage, SlugModel):
    """
    Page class
    """
    keywords = models.CharField(max_length=255, verbose_name=_('keywords'))
    description = models.CharField(
        max_length=255, verbose_name=_('description'))
