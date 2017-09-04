import pytest
from django.core.urlresolvers import reverse

from profit.lib.test import json_contains

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize('lang, content',
                         (('ru', 'Javascript язык программирования'),
                          ('en', 'Javascript programming language'), ))
def test_technologies_list(lang, content, client, settings):
    settings.LANGUAGE_CODE = lang
    response = client.get(reverse('technology-list'))
    assert response.status_code == 200
    assert len(response.json()['results']) == 2
    json_contains(response, content)


@pytest.mark.parametrize('lang, content',
                         (('ru', 'Python язык программирования'),
                          ('en', 'Python programming language'), ))
def test_technology_display(lang, content, client, settings):
    settings.LANGUAGE_CODE = lang
    response = client.get(
        reverse('technology-detail', kwargs={'slug': 'python'}))
    assert response.status_code == 200
    json_contains(response, content)
