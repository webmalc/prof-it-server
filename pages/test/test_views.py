from django.contrib.auth.models import User
from django.utils import translation

from pages.models import ExtendedFlatPage
from profit.lib.test import ViewTestCase


class PageViewTest(ViewTestCase):
    fixtures = [
        'tests/users.json',
        'tests/pages.json',
    ]

    def setUp(self):

        self.user = User.objects.get(pk=1)

    def test_admin_unauthorized_view(self):
        """
        Test payments list unauthorized view
        """
        self._test_unauthorized_view('admin:index')

    def test_index_en(self):
        """
        test main page en
        """
        url = '/en/?format=json'
        response = self.client.get(url)
        self._is_succesful(response)
        self._json_contains(response, '/en/pages')

    def test_index_ru(self):
        """
        test main page ru
        """
        url = '/ru/?format=json'
        response = self.client.get(url)
        self._is_succesful(response)
        self._json_contains(response, '/ru/pages')

    def test_pages_list_ru(self):
        """
        test pages list ru
        """
        url = '/ru/pages/?format=json'
        response = self.client.get(url)
        self._is_succesful(response)
        self._json_contains(response, 'О компании контент')
        self._json_contains(response, 'Услуги ключевые слова')

    def test_pages_list_en(self):
        """
        test pages list en
        """
        url = '/en/pages/?format=json'
        response = self.client.get(url)
        self._is_succesful(response)
        self._json_contains(response, 'About content')
        self._json_contains(response, 'Services description')

    def test_pages_display_ru(self):
        """
        test pages display en
        """
        translation.activate('ru')
        page = ExtendedFlatPage()
        page.title = 'Тестовый заголовок'
        page.content = 'Тестовый контент'
        page.url = '/url/'
        page.keywords = 'Тестовые ключевые слова'
        page.description = 'Тестовoе описание'
        page.save()

        url = '/ru/pages/testovyi-zagolovok/?format=json'
        response = self.client.get(url)
        self._is_succesful(response)
        self._json_contains(response, 'Тестовый заголовок')
        self._json_contains(response, 'Тестовый контент')
