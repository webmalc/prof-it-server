from modeltranslation.translator import TranslationOptions, register

from works.models import Technology, Work


@register(Technology)
class TechnologyTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('ru', )


@register(Work)
class WorkTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content', 'keywords',
              'meta_description')
    required_languages = ('ru', )
