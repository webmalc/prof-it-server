from django.utils import translation

from profit.lib.test import ViewTestCase
from works.models import Technology


class PageViewTest(ViewTestCase):
    fixtures = [
        'tests/technologies.json',
    ]

    def test_pages_list_ru(self):
        """
        test pages list ru
        """
        url = '/ru/technologies/?format=json'
        response = self.client.get(url)
        self._is_succesful(response)
        self._json_contains(response, 'Javascript язык программирования')
        self._json_contains(response, 'Python язык программирования')

    def test_pages_list_en(self):
        """
        test pages list en
        """
        url = '/en/technologies/?format=json'
        response = self.client.get(url)
        self._is_succesful(response)
        self._json_contains(response, 'Javascript programming language')
        self._json_contains(response, 'Python programming language')

    def test_pages_display_ru(self):
        """
        test pages display en
        """
        translation.activate('ru')
        tech = Technology()
        tech.title = 'Тестовая технология'
        tech.description = 'Описание тестовой технологии'
        tech.save()

        url = '/ru/technologies/testovaia-tekhnologiia/?format=json'
        response = self.client.get(url)
        self._is_succesful(response)
        self._json_contains(response, 'Тестовая технология')
        self._json_contains(response, 'Описание тестовой технологии')
