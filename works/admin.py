from django.contrib import admin
from modeltranslation.admin import TabbedExternalJqueryTranslationAdmin
from ordered_model.admin import OrderedModelAdmin
from reversion.admin import VersionAdmin

from .models import Technology, Work


@admin.register(Technology)
class TechnologyAdmin(VersionAdmin, TabbedExternalJqueryTranslationAdmin):
    list_display = ('id', 'title', 'slug', 'created', 'modified')
    list_filter = ('created', 'modified')
    list_display_links = ('id', 'title')
    search_fields = ('slug', 'title', 'description')
    readonly_fields = ('slug', )

    class Media:
        js = ('admin/js/works.js', )


@admin.register(Work)
class WorkAdmin(VersionAdmin, OrderedModelAdmin,
                TabbedExternalJqueryTranslationAdmin):
    list_display = ('id', 'title', 'created', 'modified', 'move_up_down_links')
    list_filter = ('created', 'modified', 'technologies')
    list_display_links = ('id', 'title')
    search_fields = ('content', 'title', 'description', 'technologies__title')

    class Media:
        js = ('admin/js/works.js', )
