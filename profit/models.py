from django.db import models
from django.template.defaultfilters import slugify
from unidecode import unidecode


class SlugModel(models.Model):
    """ Slug mixin """

    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id or not self.slug:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
