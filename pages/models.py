from django.contrib.flatpages.models import FlatPage

from profit.models import MetaModel, SlugModel


class ExtendedFlatPage(FlatPage, SlugModel, MetaModel):
    """
    Page class
    """
    pass
