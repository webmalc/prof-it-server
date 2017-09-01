import pytest
from django.core.urlresolvers import reverse

from profit.lib.test import json_contains

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize('lang, content', (('ru', 'О компании'),
                                           ('en', 'About content'), ))
def test_pages_list(lang, content, client, settings):
    settings.LANGUAGE_CODE = lang
    response = client.get(reverse('extendedflatpage-list'))
    assert response.status_code == 200
    assert len(response.json()['results']) == 2
    json_contains(response, content)


@pytest.mark.parametrize('lang, content', (('ru', 'О компании контент'),
                                           ('en', 'About keywords'), ))
def test_pages_display(lang, content, client, settings):
    settings.LANGUAGE_CODE = lang
    response = client.get(
        reverse('extendedflatpage-detail', kwargs={'slug': 'about'}))
    assert response.status_code == 200
    json_contains(response, content)
