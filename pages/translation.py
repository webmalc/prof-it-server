from django.contrib.flatpages.models import FlatPage
from modeltranslation.translator import TranslationOptions, register

from pages.models import ExtendedFlatPage


@register(FlatPage)
class BasePagesTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = ('ru', )


@register(ExtendedFlatPage)
class PagesTranslationOptions(TranslationOptions):
    fields = ('keywords', 'description')
    required_languages = ('ru', )
