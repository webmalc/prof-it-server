from rest_framework import viewsets

from works.models import Technology
from works.serializers import TechnologySerializer


class TechnologyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Technology viewset
    """
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    lookup_field = 'slug'
