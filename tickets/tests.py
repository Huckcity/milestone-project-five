from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Ticket


class UserTest(TestCase):

    @classmethod
    def setUpTestData(self):
        # Set up non-modified objects used by all test methods
        self.user = User.objects.create(
            username='user123', email='email@email.com', password='password1')

        self.bug_ticket = Ticket.objects.create(userid=self.user,
                                                title='test bug title',
                                                description='test feature description',
                                                ticket_type='Bug')

        self.feature_ticket = Ticket.objects.create(userid=self.user,
                                                    title='test feature title',
                                                    description='test feature description',
                                                    ticket_type='Feature')

    def test_create_bug_report(self):

        user = self.user
        new_ticket = Ticket.objects.create(userid=user,
                                           title='test bug title',
                                           description='test bug description',
                                           ticket_type='Bug')

        self.assertEqual(new_ticket.title, 'test bug title')

    def test_create_feature_request(self):

        user = self.user
        new_ticket = Ticket.objects.create(userid=user,
                                           title='test feature title',
                                           description='test feature description',
                                           ticket_type='Feature')

        self.assertEqual(new_ticket.title, 'test feature title')

    def test_create_ticket_without_type(self):

        user = self.user
        new_ticket = Ticket.objects.create(userid=user,
                                           title='test feature title',
                                           description='test feature description')

        self.assertRaises(ValidationError, new_ticket.full_clean)

    def test_create_ticket_has_default_status_pending(self):

        new_ticket = self.bug_ticket

        self.assertEqual(new_ticket.status, 'Pending')
