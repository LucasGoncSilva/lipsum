from django.test import TestCase
from django.urls import reverse

from account.models import User


# Create your tests here.
class AccountViewsTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(
            username='test_user',
            password='superhyperultrahardpassword',
            first_name='Otto',
            last_name='with an O',
            email='test_user@example.com'
        )

    def test_register_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/conta/registrar" for not logged and logged users"""

        res = self.client.get(reverse('account:register'))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/register.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('account:register'))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('home:index'))

        res = self.client.get(reverse('account:register'), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home/index.html')

    def test_login_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/conta/entrar" for not logged and logged users"""

        res = self.client.get(reverse('account:login'))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('account:login'))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('home:index'))

        res = self.client.get(reverse('account:login'), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home/index.html')

    def test_logout_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/conta/sair" for not logged and logged users"""

        res = self.client.get(reverse('account:logout'))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('account:logout'))

        res = self.client.get(reverse('account:logout'), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('account:logout'))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/logout.html')
