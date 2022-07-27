from django.test import TestCase
from django.urls import reverse

from account.models import User
from secret.models import Card, LoginCredential, SecurityNote
from secret.month.models import Month


# Create your tests here.
class SecretIndexViewTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(
            username='test_user',
            password='superhyperultrahardpassword',
            first_name='Otto',
            last_name='with an O',
            email='test_user@example.com'
        )

    def test_index_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/segredo/" for not logged and logged users"""

        res = self.client.get(reverse('secret:index'))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('secret:index'))

        res = self.client.get(reverse('secret:index'), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('secret:index'))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'secret/index.html')


class LoginCredentialViewsTestCase(TestCase):
    def setUp(self) -> None:
        test_user = User.objects.create_user(
            username='test_user',
            password='superhyperultrahardpassword',
            first_name='Otto',
            last_name='with an O',
            email='test_user@example.com'
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

    def test_credential_create_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/segredo/credenciais/nova" for not logged and logged users"""

        res = self.client.get(reverse('secret:credential_create_view'))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('secret:credential_create_view'))

        res = self.client.get(reverse('secret:credential_create_view'), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('secret:credential_create_view'))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'secret/create_view.html')

        self.assertIn('action', res.context.keys())
        self.assertEqual(res.context['action'], 'Adição')

        self.assertIn('model', res.context.keys())
        self.assertEqual(res.context['model'], 'Credencial')

    def test_credential_list_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/segredo/credenciais/" for not logged and logged users"""

        res = self.client.get(reverse('secret:credential_list_view'))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('secret:credential_list_view'))

        res = self.client.get(reverse('secret:credential_list_view'), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('secret:credential_list_view'))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'secret/list_view.html')

        self.assertIn('object_list', res.context.keys())
        self.assertEqual(len(res.context['object_list']), 2)

        self.assertIn('model_name', res.context.keys())
        self.assertEqual(res.context['model_name'], 'Credenciais')

    def test_credential_detail_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/segredo/credenciais/<slug:slug>" for not logged and logged users"""

        res = self.client.get(reverse('secret:credential_detail_view', kwargs={'slug': 'google--personal-main-account'}))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('secret:credential_detail_view', kwargs={'slug': 'google--personal-main-account'}))

        res = self.client.get(reverse('secret:credential_detail_view', kwargs={'slug': 'google--personal-main-account'}), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('secret:credential_detail_view', kwargs={'slug': 'google--personal-main-account'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'secret/Credential/detail_view.html')

        self.assertIn('object', res.context.keys())
        self.assertEqual(res.context['object'], LoginCredential.objects.get(owner=User.objects.first(), slug='google--personal-main-account'))

        res = self.client.get(reverse('secret:credential_detail_view', kwargs={'slug': 'lasagna--double-pizza'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'err/error_template.html')

    def test_credential_update_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/segredo/credenciais/<slug:slug>/editar" for not logged and logged users"""

        res = self.client.get(reverse('secret:credential_update_view', kwargs={'slug': 'google--personal-main-account'}))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('secret:credential_update_view', kwargs={'slug': 'google--personal-main-account'}))

        res = self.client.get(reverse('secret:credential_update_view', kwargs={'slug': 'google--personal-main-account'}), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('secret:credential_update_view', kwargs={'slug': 'google--personal-main-account'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'secret/create_view.html')

        self.assertIn('action', res.context.keys())
        self.assertEqual(res.context['action'], 'Edição')

        self.assertIn('model', res.context.keys())
        self.assertEqual(res.context['model'], 'Credencial')

        self.assertIn('object', res.context.keys())
        self.assertEqual(res.context['object'], LoginCredential.objects.get(owner=User.objects.first(), slug='google--personal-main-account'))

        res = self.client.get(reverse('secret:credential_update_view', kwargs={'slug': 'lasagna--double-pizza'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'err/error_template.html')

    def test_credential_delete_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/segredo/credenciais/<slug:slug>/deletar" for not logged and logged users"""

        res = self.client.get(reverse('secret:credential_delete_view', kwargs={'slug': 'google--personal-main-account'}))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('secret:credential_delete_view', kwargs={'slug': 'google--personal-main-account'}))

        res = self.client.get(reverse('secret:credential_delete_view', kwargs={'slug': 'google--personal-main-account'}), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('secret:credential_delete_view', kwargs={'slug': 'google--personal-main-account'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'secret/delete_view.html')

        self.assertIn('action', res.context.keys())
        self.assertEqual(res.context['action'], 'Exclusão')

        self.assertIn('model', res.context.keys())
        self.assertEqual(res.context['model'], 'Credencial')

        self.assertIn('object', res.context.keys())
        self.assertEqual(res.context['object'], LoginCredential.objects.get(owner=User.objects.first(), slug='google--personal-main-account'))

        res = self.client.get(reverse('secret:credential_delete_view', kwargs={'slug': 'lasagna--double-pizza'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'err/error_template.html')


class CardViewsTestCase(TestCase):
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

    def test_card_create_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/segredo/cartoes/novo" for not logged and logged users"""

        res = self.client.get(reverse('secret:card_create_view'))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('secret:card_create_view'))

        res = self.client.get(reverse('secret:card_create_view'), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('secret:card_create_view'))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'secret/create_view.html')

        self.assertIn('action', res.context.keys())
        self.assertEqual(res.context['action'], 'Adição')

        self.assertIn('model', res.context.keys())
        self.assertEqual(res.context['model'], 'Cartão')

    def test_card_list_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/segredo/cartoes/" for not logged and logged users"""

        res = self.client.get(reverse('secret:card_list_view'))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('secret:card_list_view'))

        res = self.client.get(reverse('secret:card_list_view'), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('secret:card_list_view'))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'secret/list_view.html')

        self.assertIn('object_list', res.context.keys())
        self.assertEqual(len(res.context['object_list']), 1)

        self.assertIn('model_name', res.context.keys())
        self.assertEqual(res.context['model_name'], 'Cartões')

    def test_card_detail_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/segredo/cartoes/<slug:slug>" for not logged and logged users"""

        res = self.client.get(reverse('secret:card_detail_view', kwargs={'slug': 'nubank--personal-main-card'}))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('secret:card_detail_view', kwargs={'slug': 'nubank--personal-main-card'}))

        res = self.client.get(reverse('secret:card_detail_view', kwargs={'slug': 'nubank--personal-main-card'}), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('secret:card_detail_view', kwargs={'slug': 'nubank--personal-main-card'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'secret/Card/detail_view.html')

        self.assertIn('object', res.context.keys())
        self.assertEqual(res.context['object'], Card.objects.get(owner=User.objects.first(), slug='nubank--personal-main-card'))

        res = self.client.get(reverse('secret:card_detail_view', kwargs={'slug': 'lasagna--double-pizza'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'err/error_template.html')

    def test_card_update_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/segredo/cartoes/<slug:slug>/editar" for not logged and logged users"""

        res = self.client.get(reverse('secret:card_update_view', kwargs={'slug': 'nubank--personal-main-card'}))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('secret:card_update_view', kwargs={'slug': 'nubank--personal-main-card'}))

        res = self.client.get(reverse('secret:card_update_view', kwargs={'slug': 'nubank--personal-main-card'}), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('secret:card_update_view', kwargs={'slug': 'nubank--personal-main-card'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'secret/create_view.html')

        self.assertIn('action', res.context.keys())
        self.assertEqual(res.context['action'], 'Edição')

        self.assertIn('model', res.context.keys())
        self.assertEqual(res.context['model'], 'Cartão')

        self.assertIn('object', res.context.keys())
        self.assertEqual(res.context['object'], Card.objects.get(owner=User.objects.first(), slug='nubank--personal-main-card'))

        res = self.client.get(reverse('secret:card_update_view', kwargs={'slug': 'lasagna--double-pizza'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'err/error_template.html')

    def test_card_delete_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/segredo/cartoes/<slug:slug>/deletar" for not logged and logged users"""

        res = self.client.get(reverse('secret:card_delete_view', kwargs={'slug': 'nubank--personal-main-card'}))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('secret:card_delete_view', kwargs={'slug': 'nubank--personal-main-card'}))

        res = self.client.get(reverse('secret:card_delete_view', kwargs={'slug': 'nubank--personal-main-card'}), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('secret:card_delete_view', kwargs={'slug': 'nubank--personal-main-card'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'secret/delete_view.html')

        self.assertIn('action', res.context.keys())
        self.assertEqual(res.context['action'], 'Exclusão')

        self.assertIn('model', res.context.keys())
        self.assertEqual(res.context['model'], 'Cartão')

        self.assertIn('object', res.context.keys())
        self.assertEqual(res.context['object'], Card.objects.get(owner=User.objects.first(), slug='nubank--personal-main-card'))

        res = self.client.get(reverse('secret:card_delete_view', kwargs={'slug': 'lasagna--double-pizza'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'err/error_template.html')


class SecurityNoteViewsTestCase(TestCase):
    def setUp(self) -> None:
        test_user = User.objects.create_user(
            username='test_user',
            password='superhyperultrahardpassword',
            first_name='Otto',
            last_name='with an O',
            email='test_user@example.com'
        )

        SecurityNote.objects.create(
            owner=test_user,
            title='How to draw an apple',
            slug='how-to-draw-an-apple',
            content='Just draw an apple tree and erase the tree.'
        )

    def test_note_create_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/segredo/anotacoes/novo" for not logged and logged users"""

        res = self.client.get(reverse('secret:note_create_view'))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('secret:note_create_view'))

        res = self.client.get(reverse('secret:note_create_view'), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('secret:note_create_view'))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'secret/create_view.html')

        self.assertIn('action', res.context.keys())
        self.assertEqual(res.context['action'], 'Adição')

        self.assertIn('model', res.context.keys())
        self.assertEqual(res.context['model'], 'Anotação')

    def test_note_list_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/segredo/anotacoes/" for not logged and logged users"""

        res = self.client.get(reverse('secret:note_list_view'))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('secret:note_list_view'))

        res = self.client.get(reverse('secret:note_list_view'), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('secret:note_list_view'))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'secret/list_view.html')

        self.assertIn('object_list', res.context.keys())
        self.assertEqual(len(res.context['object_list']), 1)

        self.assertIn('model_name', res.context.keys())
        self.assertEqual(res.context['model_name'], 'Anotações')

    def test_note_detail_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/segredo/anotacoes/<slug:slug>" for not logged and logged users"""

        res = self.client.get(reverse('secret:note_detail_view', kwargs={'slug': 'how-to-draw-an-apple'}))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('secret:note_detail_view', kwargs={'slug': 'how-to-draw-an-apple'}))

        res = self.client.get(reverse('secret:note_detail_view', kwargs={'slug': 'how-to-draw-an-apple'}), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('secret:note_detail_view', kwargs={'slug': 'how-to-draw-an-apple'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'secret/Note/detail_view.html')

        self.assertIn('object', res.context.keys())
        self.assertEqual(res.context['object'], SecurityNote.objects.get(owner=User.objects.first(), slug='how-to-draw-an-apple'))

        res = self.client.get(reverse('secret:note_detail_view', kwargs={'slug': 'lasagna--double-pizza'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'err/error_template.html')

    def test_note_update_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/segredo/anotacoes/<slug:slug>/editar" for not logged and logged users"""

        res = self.client.get(reverse('secret:note_update_view', kwargs={'slug': 'how-to-draw-an-apple'}))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('secret:note_update_view', kwargs={'slug': 'how-to-draw-an-apple'}))

        res = self.client.get(reverse('secret:note_update_view', kwargs={'slug': 'how-to-draw-an-apple'}), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('secret:note_update_view', kwargs={'slug': 'how-to-draw-an-apple'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'secret/create_view.html')

        self.assertIn('action', res.context.keys())
        self.assertEqual(res.context['action'], 'Edição')

        self.assertIn('model', res.context.keys())
        self.assertEqual(res.context['model'], 'Anotação')

        self.assertIn('object', res.context.keys())
        self.assertEqual(res.context['object'], SecurityNote.objects.get(owner=User.objects.first(), slug='how-to-draw-an-apple'))

        res = self.client.get(reverse('secret:note_update_view', kwargs={'slug': 'lasagna--double-pizza'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'err/error_template.html')

    def test_note_delete_view_behavior_for_not_logged_and_logged_users(self):
        """Tests view behavior at "/segredo/anotacoes/<slug:slug>/deletar" for not logged and logged users"""

        res = self.client.get(reverse('secret:note_delete_view', kwargs={'slug': 'how-to-draw-an-apple'}))

        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, reverse('account:login') + '?next=' + reverse('secret:note_delete_view', kwargs={'slug': 'how-to-draw-an-apple'}))

        res = self.client.get(reverse('secret:note_delete_view', kwargs={'slug': 'how-to-draw-an-apple'}), follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/login.html')

        self.client.login(
            username='test_user',
            password='superhyperultrahardpassword'
        )

        res = self.client.get(reverse('secret:note_delete_view', kwargs={'slug': 'how-to-draw-an-apple'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'secret/delete_view.html')

        self.assertIn('action', res.context.keys())
        self.assertEqual(res.context['action'], 'Exclusão')

        self.assertIn('model', res.context.keys())
        self.assertEqual(res.context['model'], 'Anotação')

        self.assertIn('object', res.context.keys())
        self.assertEqual(res.context['object'], SecurityNote.objects.get(owner=User.objects.first(), slug='how-to-draw-an-apple'))

        res = self.client.get(reverse('secret:note_delete_view', kwargs={'slug': 'lasagna--double-pizza'}))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'err/error_template.html')
