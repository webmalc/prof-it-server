from rest_framework import viewsets

from .models import ExtendedFlatPage
from .serializers import PageSerializer


class PagesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Pages viewset
    """
    queryset = ExtendedFlatPage.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'
