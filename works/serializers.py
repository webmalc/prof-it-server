from rest_framework import serializers

from .models import Photo, Technology, Work


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
    photos = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='photo-detail')

    class Meta:
        model = Work
        fields = ('id', 'title', 'description', 'content', 'created',
                  'modified', 'meta_description', 'keywords', 'technologies',
                  'is_enabled', 'photos')


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    work = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name='work-detail')
    thumbnail = serializers.ImageField(read_only=True)
    thumbnail_xs = serializers.ImageField(read_only=True)
    preview_photo = serializers.ImageField(read_only=True)

    class Meta:
        model = Photo
        fields = ('id', 'work', 'title', 'description', 'is_default', 'photo',
                  'thumbnail', 'thumbnail_xs', 'preview_photo')
