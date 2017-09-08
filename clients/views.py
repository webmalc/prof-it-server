from rest_framework import mixins, viewsets

from .models import Email
from .serializers import EmailSerializer


class EmailViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Email viewset
    """
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
