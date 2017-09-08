from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class Email(TimeStampedModel):
    """ Email class """
    name = models.CharField(_('name'), max_length=255, db_index=True)
    subject = models.CharField(
        _('subject'),
        max_length=255,
        default=_('Email from client'),
        db_index=True)
    contacts = models.CharField(_('contacts'), max_length=255, db_index=True)
    text = models.TextField(_('text'), max_length=255, db_index=True)
    is_readed = models.BooleanField(
        ('is readed?'), default=False, db_index=True)
    ip = models.GenericIPAddressField(null=True, blank=True, db_index=True)

    def __str__(self):
        return '#{id} {subject} {name} ({contacts}) {date}'.format(
            id=self.id,
            subject=self.subject,
            name=self.name,
            contacts=self.contacts,
            date=self.created.strftime('%c'))
