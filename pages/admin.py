from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.forms import FlatpageForm
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from reversion.admin import VersionAdmin

from pages.models import ExtendedFlatPage


class ExtendedFlatPageForm(FlatpageForm):
    class Meta:
        model = ExtendedFlatPage
        fields = '__all__'


class ExtendedFlatPageAdmin(FlatPageAdmin, VersionAdmin):
    form = ExtendedFlatPageForm
    list_display = ('id', 'title', 'slug', 'url')
    list_display_links = ('id', 'title')
    readonly_fields = ('slug', )
    fieldsets = ((None, {
        'fields': ('url', 'title', 'slug', 'content', 'sites')
    }), (_('Advanced options'), {
        'classes': ('collapse', ),
        'fields':
        ('keywords', 'description', 'registration_required', 'template_name'),
    }), )

    class Media:
        js = ('admin/js/pages.js', )


admin.site.unregister(FlatPage)
admin.site.register(ExtendedFlatPage, ExtendedFlatPageAdmin)
