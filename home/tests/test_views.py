from django.test import TestCase
from django.urls import reverse

from account.models import User
from secret.models import Card, LoginCredential, SecurityNote
from secret.month.models import Month


# Create your tests here.
class HomeViewsTestCase(TestCase):
    def setUp(self) -> None:
        test_user = User.objects.create_user(
            username='test_user',
            password='superhyperultrahardpassword',
            first_name='Otto',
            last_name='with an O',
            email='test_user@example.com'
        )

        Card.objects.create(
            owner=test_user,
            name='Personal Main Card',
            card_type='deb',
            number='4002892240028922',
            expiration=Month(2028, 11),
            cvv='113',
            bank='nubank--',
            brand='mastercard--',
            slug='nubank--personal-main-card',
            owners_name='TEST USER',
        )

        LoginCredential.objects.create(
            owner=test_user,
            service='google--',
            name='Personal Main Account',
            slug='google--personal-main-account',
            thirdy_party_login=False,
            thirdy_party_login_name='-----',
            login='night_monkey123@gmail.com',
            password='ilovemenotyou',
        )

        LoginCredential.objects.create(
            owner=test_user,
            service='steam--',
            name='Little Fries',
            slug='steam--little-fries',
            thirdy_party_login=True,
            thirdy_party_login_name='Personal Main Account',
            login='-----',
            password='-----',
        )

        SecurityNote.objects.create(
            owner=test_user,
            title='How to draw an apple',
            slug='how-to-draw-an-apple',
            content='Just draw an apple tree and erase the tree.'
        )

    def test_home_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/" for not logged and logged users"""

        res = self.client.get(reverse('home:index'))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home/landing.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('home:index'))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home/index.html')

        self.assertIn('cards', res.context.keys())
        self.assertIn('credentials', res.context.keys())
        self.assertIn('notes', res.context.keys())

        self.assertEqual(len(res.context['cards']), 1)
        self.assertEqual(len(res.context['credentials']), 2)
        self.assertEqual(len(res.context['notes']), 1)