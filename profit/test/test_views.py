import pytest
from django.core.urlresolvers import reverse
from profit.lib.test import json_contains


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
