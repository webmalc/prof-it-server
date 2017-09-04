import pytest
from django.core.urlresolvers import reverse

from profit.lib.test import json_contains

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize('lang, content', (('ru', 'Тестовая работа 1'),
                                           ('en', 'Test work 3 - content'), ))
def test_works_list(lang, content, client, settings):
    settings.LANGUAGE_CODE = lang
    response = client.get(reverse('work-list'))
    assert response.status_code == 200
    assert len(response.json()['results']) == 3
    json_contains(response, content)


@pytest.mark.parametrize('lang, content',
                         (('ru', 'Тестовая работа 2 - описание'),
                          ('en', 'Test work 2 - keywords'), ))
def test_work_display(lang, content, client, settings):
    settings.LANGUAGE_CODE = lang
    response = client.get(reverse('work-detail', kwargs={'pk': 2}))
    assert response.status_code == 200
    json_contains(response, content)
