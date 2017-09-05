from rest_framework import serializers

from .models import ExtendedFlatPage


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExtendedFlatPage
        fields = ('id', 'url', 'title', 'slug', 'content', 'keywords',
                  'meta_description', 'registration_required', 'is_enabled')
        lookup_field = 'slug'
