from django.test import TestCase


class StaticPageTest(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_status_code(self):
        response = self.client.get('/accounts/login')
        self.assertEqual(response.status_code, 200)

    def test_register_page_status_code(self):
        response = self.client.get('/accounts/register')
        self.assertEqual(response.status_code, 200)
