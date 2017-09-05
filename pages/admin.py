from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.forms import FlatpageForm
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from modeltranslation.admin import TabbedExternalJqueryTranslationAdmin
from reversion.admin import VersionAdmin

from .models import ExtendedFlatPage


class ExtendedFlatPageForm(FlatpageForm):
    class Meta:
        model = ExtendedFlatPage
        fields = '__all__'


class ExtendedFlatPageAdmin(FlatPageAdmin, VersionAdmin,
                            TabbedExternalJqueryTranslationAdmin):
    form = ExtendedFlatPageForm
    list_display = ('id', 'title', 'slug', 'url')
    list_display_links = ('id', 'title')
    readonly_fields = ('slug', )
    search_fields = ('url', 'title', 'slug', 'content')
    fieldsets = ((None, {
        'fields': ('url', 'title', 'slug', 'content', 'sites', 'keywords',
                   'meta_description')
    }), (_('Advanced options'), {
        'classes': ('collapse', ),
        'fields': ('registration_required', 'template_name'),
    }), )

    class Media:
        js = ('admin/js/pages.js', )


admin.site.unregister(FlatPage)
admin.site.register(ExtendedFlatPage, ExtendedFlatPageAdmin)
