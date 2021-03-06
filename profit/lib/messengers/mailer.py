import logging

from django.conf import settings
from django.core.mail import mail_managers as base_mail_managers
from django.core.mail import send_mail
from django.template.loader import render_to_string


def mail_managers(subject, template='emails/base_manager.html', data=None):
    base_mail_managers(
        subject=subject,
        message='',
        html_message=render_to_string(template, data if data else {}))
    logging.getLogger('profit').info(
        'Send mail to managers. Subject: {}'.format(subject))


def mail_client(subject, template, data, email=None, client=None):
    send_mail(
        recipient_list=[email] if email else [client.email],
        from_email=settings.DEFAULT_FROM_EMAIL,
        subject='{prefix}{text}'.format(
            prefix=settings.EMAIL_SUBJECT_PREFIX, text=subject),
        message='',
        html_message=render_to_string(template, data))
    logging.getLogger('profit').info(
        'Send mail to client. Subject: {}; client: {}; email: {};'.format(
            subject, client, email))
