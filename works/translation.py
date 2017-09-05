from modeltranslation.translator import TranslationOptions, register

from .models import Photo, Technology, Work


@register(Technology)
class TechnologyTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('ru', )


@register(Work)
class WorkTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content', 'keywords',
              'meta_description')
    required_languages = ('ru', )


@register(Photo)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('ru', )
