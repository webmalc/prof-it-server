from rest_framework import viewsets

from pages.models import ExtendedFlatPage
from pages.serializers import PageSerializer


class PagesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Pages viewset
    """
    queryset = ExtendedFlatPage.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'
