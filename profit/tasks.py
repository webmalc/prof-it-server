from __future__ import absolute_import

from profit.celery import app
from profit.lib.messengers.mailer import mail_managers


@app.task
def mail_managers_task(subject, template, data):
    """
    Mail to site managers
    :param subject: subject string
    :param template: template name
    :param data: data dict for template rendering
    """
    mail_managers(subject=subject, template=template, data=data)
