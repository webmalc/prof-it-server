from django.conf import settings
from django.utils import translation


class AdminLocaleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin'):
            request.LANG = getattr(settings, 'ADMIN_LANGUAGE_CODE',
                                   settings.LANGUAGE_CODE)
            translation.activate(request.LANG)
            request.LANGUAGE_CODE = request.LANG
        else:
            request.LANG = settings.LANGUAGE_CODE
            translation.activate(request.LANG)
            request.LANGUAGE_CODE = request.LANG

        return self.get_response(request)
