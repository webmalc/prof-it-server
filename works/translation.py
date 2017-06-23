from modeltranslation.translator import TranslationOptions, register

from works.models import Technology


@register(Technology)
class TechnologyTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('ru', )
