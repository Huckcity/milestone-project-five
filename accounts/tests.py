from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserTest(TestCase):

    def setUp(self):
        self.good_credentials = {
            'username': 'testuser1',
            'password': 'secret'}
        self.bad_credentials = {
            'username': 'testuser2',
            'password': ''}

        User.objects.create_user(**self.good_credentials)
        User.objects.create_user(**self.bad_credentials)

    def test_login_form(self):
        response = self.client.post('/accounts/login/', self.good_credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_login_form_with_bad_data(self):
        response = self.client.post('/accounts/login/', self.bad_credentials, follow=True)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_registration_form_with_data(self):
        form = UserCreationForm({
            'username': 'test',
            'email': 'test@example.com',
            'password1': 'example1',
            'password2': 'example1',
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_with_no_email(self):
        form = UserCreationForm({
            'username': '',
            'email': 'test@example.com',
            'password1': 'example1',
            'password2': 'example1',
        })
        self.assertFalse(form.is_valid())

    def test_registration_form_passwords_dont_match(self):
        form = UserCreationForm({
            'username': '',
            'email': 'test@example.com',
            'password1': 'example1',
            'password2': 'example2',
        })
        self.assertFalse(form.is_valid())
