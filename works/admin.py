from django.contrib import admin
from modeltranslation.admin import (TabbedExternalJqueryTranslationAdmin,
                                    TranslationTabularInline)
from ordered_model.admin import OrderedModelAdmin
from reversion.admin import VersionAdmin

from .models import Photo, Technology, Work


@admin.register(Technology)
class TechnologyAdmin(VersionAdmin, TabbedExternalJqueryTranslationAdmin):
    list_display = ('id', 'title', 'slug', 'created', 'modified')
    list_filter = ('created', 'modified')
    list_display_links = ('id', 'title')
    search_fields = ('slug', 'title', 'description')
    readonly_fields = ('slug', )

    class Media:
        js = ('admin/js/works.js', )


class PhotoInline(TranslationTabularInline):
    """
    Work photos admin
    """
    model = Photo
    fields = ('title', 'photo_tag', 'photo', 'is_default')
    readonly_fields = ('photo_tag', )


@admin.register(Work)
class WorkAdmin(VersionAdmin, OrderedModelAdmin,
                TabbedExternalJqueryTranslationAdmin):
    list_display = ('id', 'title', 'created', 'modified', 'is_enabled',
                    'move_up_down_links')
    list_filter = ('created', 'modified', 'technologies', 'is_enabled', )
    list_display_links = ('id', 'title')
    search_fields = ('content', 'title', 'description', 'technologies__title')
    inlines = (PhotoInline, )
    fieldsets = (('General', {
        'fields':
        ('title', 'description', 'content', 'technologies', 'is_enabled', )
    }), ('Meta', {
        'fields': ('keywords', 'meta_description', )
    }), )

    class Media:
        js = ('admin/js/works.js', )
