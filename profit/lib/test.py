from django.core.urlresolvers import reverse
from django.test import TestCase, override_settings, tag


@tag('unit', 'view')
@override_settings(CELERY_ALWAYS_EAGER=True)
class ViewTestCase(TestCase):
    def _test_unauthorized_view(self,
                                route_name,
                                redirect_route='admin:login',
                                params={}):
        url = reverse(route_name, kwargs=params)
        redirect = reverse(redirect_route) + '?next=' + url
        response = self.client.get(url)
        assert response.url == redirect
        assert response.status_code == 302

    def _login_superuser(self):
        login = self.client.login(username='admin', password='password')
        assert login

    def _is_succesful(self, response, title=None):
        """
        :param response: django response
        :param title: html title
        :type title: string or none
        """
        assert response.status_code == 200
        if title:
            assert title in response.body

    def __check_dict(self, data, search):
        """
        search dict for value
        :param data: dict
        :param search: search string value
        """
        return len(
            [x for x in data.values() if type(x) == str and search in x]) > 0

    def _json_contains(self, response, search):
        """
        search json response for value
        :param response: django response
        :param search: search string value
        """
        result = False
        data = response.json()
        if 'results' in data:
            data = data['results']

        if type(data) == list:
            for entry in data:
                result = self.__check_dict(entry, search)
                if result:
                    break
        else:
            result = self.__check_dict(data, search)
        assert result


@tag('unit', 'form')
class FormTestCase(TestCase):
    pass


@tag('unit', 'task')
@override_settings(CELERY_ALWAYS_EAGER=True)
class TaskTestCase(TestCase):
    pass


@tag('unit', 'model')
class ModelTestCase(TestCase):
    pass
