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


class WorkViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Work viewset
    """
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
