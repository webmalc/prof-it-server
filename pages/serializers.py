from rest_framework import serializers

from pages.models import ExtendedFlatPage


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExtendedFlatPage
        fields = ('url', 'title', 'slug', 'content', 'keywords', 'description',
                  'registration_required')
        lookup_field = 'slug'
