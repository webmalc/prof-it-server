import pytest
from django.core.urlresolvers import reverse

from profit.lib.test import json_contains

pytestmark = pytest.mark.django_db


def test_admin_view_by_admin(admin_client):
    response = admin_client.get(reverse('admin:index'))
    assert response.status_code == 200


def test_admin_view_by_user(client):
    response = client.get(reverse('admin:index'))
    assert response.status_code == 302


@pytest.mark.parametrize('lang', ('ru', 'en'))
def test_main_view_by_admin(lang, admin_client, settings):
    settings.LANGUAGE_CODE = lang
    response = admin_client.get(reverse('api-root'))
    assert response.status_code == 200
    json_contains(response, '/{}/pages'.format(lang))
    json_contains(response, '/{}/works'.format(lang))
    json_contains(response, '/{}/technologies'.format(lang))


@pytest.mark.parametrize(
    'lang, content, url, records',
    (('ru', 'Тестовая работа 1', 'work-list', 3),
     ('en', 'Test work 3 - content', 'work-list', 3),
     ('ru', 'О компании', 'extendedflatpage-list', 2),
     ('en', 'About content', 'extendedflatpage-list', 2),
     ('ru', 'Javascript язык программирования', 'technology-list', 2),
     ('en', 'Python programming language', 'technology-list', 2), ))
def test_generic_list(lang, content, url, records, client, settings):
    settings.LANGUAGE_CODE = lang
    response = client.get(reverse(url))
    assert response.status_code == 200
    assert len(response.json()['results']) == records
    json_contains(response, content)


@pytest.mark.parametrize('lang, content, url, key', (
    ('ru', 'Тестовая работа 2 - описание', 'work-detail', {
        'pk': 2
    }), ('en', 'Test work 2 - keywords', 'work-detail', {
        'pk': 2
    }), ('ru', 'Python язык программирования', 'technology-detail', {
        'slug': 'python'
    }), ('en', 'Python programming language', 'technology-detail', {
        'slug': 'python'
    }), ('en', 'About keywords', 'extendedflatpage-detail', {
        'slug': 'about'
    }), ('ru', 'О компании контент', 'extendedflatpage-detail', {
        'slug': 'about'
    }), ))
def test_generic_display(lang, content, url, key, client, settings):
    settings.LANGUAGE_CODE = lang
    response = client.get(reverse(url, kwargs=key))
    assert response.status_code == 200
    json_contains(response, content)
