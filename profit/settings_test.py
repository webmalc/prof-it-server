from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_ndptc'
    }
}

ADMINS = (('admin', 'admin@example.com'), ('manager', 'manager@example.com'))
MANAGERS = ADMINS

LOGGING.pop('root', None)
CELERY_ALWAYS_EAGER = True
