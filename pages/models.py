from django.contrib.flatpages.models import FlatPage

from profit.models import KeywordsDescModel, SlugModel


class ExtendedFlatPage(FlatPage, SlugModel, KeywordsDescModel):
    """
    Page class
    """
    pass
