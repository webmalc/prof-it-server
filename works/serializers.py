from rest_framework import serializers

from .models import Technology, Work


class TechnologySerializer(serializers.HyperlinkedModelSerializer):
    works = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='work-detail')

    class Meta:
        model = Technology
        fields = ('id', 'title', 'slug', 'description', 'created', 'modified',
                  'works')
        lookup_field = 'slug'


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    technologies = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='slug')

    class Meta:
        model = Work
        fields = ('id', 'title', 'description', 'content', 'created',
                  'modified', 'meta_description', 'keywords', 'technologies',
                  'is_enabled')
