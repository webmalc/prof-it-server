DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'profit',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mail@vishleva.com'
EMAIL_HOST_PASSWORD = 'nnmessdytpcxlepw'
DEFAULT_FROM_EMAIL = 'vishleva.com <mail@vishleva.com>'
SERVER_EMAIL = 'vishleva.com <mail@vishleva.com>'

ADMINS = (('prof-it.group', 'm@webmalc.pw'), )
MANAGERS = ADMINS

SECRET_KEY = 'my_super_secret_key'
ALLOWED_HOSTS = ['*']
DEBUG = True
