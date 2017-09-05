from rest_framework import viewsets

from .models import Technology, Work
from .serializers import TechnologySerializer, WorkSerializer


class TechnologyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Technology viewset
    """
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    lookup_field = 'slug'
    search_fields = ('slug', 'title', 'description')


class WorkViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Work viewset
    """
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    search_fields = ('content', 'title', 'description', 'technologies__title')
    filter_fields = ('technologies', 'is_enabled')
