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
    search_fields = ('url', 'title', 'slug', 'content')
    filter_fields = ('is_enabled', )
