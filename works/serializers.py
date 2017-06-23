from rest_framework import serializers

from works.models import Technology


class TechnologySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Technology
        fields = ('id', 'title', 'slug', 'description', 'created', 'modified')
        lookup_field = 'slug'
