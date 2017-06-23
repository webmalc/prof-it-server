from django.contrib import admin
from modeltranslation.admin import TabbedExternalJqueryTranslationAdmin
from reversion.admin import VersionAdmin

from works.models import Technology


@admin.register(Technology)
class TechnologyAdmin(VersionAdmin, TabbedExternalJqueryTranslationAdmin):
    list_display = ('id', 'title', 'slug', 'created', 'modified')
    list_filter = ('created', 'modified')
    list_display_links = ('id', 'title')
    search_fields = ('slug', 'title', 'description')
    readonly_fields = ('slug', )
