from django.contrib import admin
from reversion.admin import VersionAdmin

from .models import Email


@admin.register(Email)
class EmailAdmin(VersionAdmin):
    list_display = ('id', 'name', 'contacts', 'subject', 'is_readed',
                    'created')
    list_filter = ('is_readed', 'created', 'modified')
    list_display_links = ('id', 'subject', 'name')
    search_fields = ('id', 'name', 'contacts', 'subject', 'text', 'ip', 'text')
    readonly_fields = ('created', 'modified')
    fieldsets = (('General', {
        'fields': ('subject', 'name', 'contacts', 'text')
    }), ('Options', {
        'fields': ('ip', 'is_readed', 'created', 'modified')
    }), )

    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        initial.setdefault('is_readed', True)
        return initial

    def changeform_view(self,
                        request,
                        object_id=None,
                        form_url='',
                        extra_context=None):
        if object_id:
            Email.objects.filter(
                pk=object_id, is_readed=False).update(is_readed=True)
        return super().changeform_view(request, object_id, form_url,
                                       extra_context)

    class Media:
        js = ('admin/js/clients.js', )
