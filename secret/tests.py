from django.test import TestCase

from accounts.models import User
from .models import Card, LoginCredential
from .month.models import Month


# Create your tests here.
class CredentialTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create(
            username='test_user',
            password='testing_password',
            email='test@email.com',
            first_name='Test',
            last_name='User'
        )

        LoginCredential.objects.create(
            owner=test_user,
            service='google-',
            name='Personal Main Account',
            slug='google--personal-main-account',
            thirdy_party_login=False,
            thirdy_party_login_name='-----',
            login='night_monkey123@gmail.com',
            password='ilovemenotyou',
        )  # Correct object

        LoginCredential.objects.create(
            owner=test_user,
            service='steam-',
            name='Little Fries',
            slug='steam--little-fries',
            thirdy_party_login=True,
            thirdy_party_login_name='Personal Main Account',
            login='-----',
            password='-----',
        )  # Correct object

        LoginCredential.objects.create(
            owner=test_user,
            service='steam-',
            name='Little Fries',
            slug='steam--little-fries',
            thirdy_party_login=True,  # Should be False or...
            thirdy_party_login_name='-----',  # Should be something different to '-----'
            login='night_monkey123',  # Should be '-----'
            password='ilovemenotyou',  # Should be '-----'
        )

        LoginCredential.objects.create(
            owner=test_user,
            service='steam-',
            name='Little Fries',
            slug='steam--potato',  # Should be 'steam--little-fries'
            thirdy_party_login=False,
            thirdy_party_login_name='-----',
            login='',  # Empty login
            password='night_monkey123',
        )

        LoginCredential.objects.create(
            owner=test_user,
            service='steam-',
            name='Little Fries',
            slug='steam--little-fries',
            thirdy_party_login=False,
            thirdy_party_login_name='-----',
            login='night_monkey123',
            # Missing/empty password
        )

        LoginCredential.objects.create(
            owner=test_user,
            service='google-',
            name='Salve'*9,  # More chars than the limit
            slug='google--personal-main-account',
            thirdy_party_login=False,
            thirdy_party_login_name='-----',
            login='x'*201,  # More chars than the limit
            password='ilovemenotyou',
        )

        LoginCredential.objects.create(
            owner=test_user,
            service='pampas-gonden-radio-',  # Inexistent service
            name='Little Fries',
            slug='pampas-gonden-radio--little-fries',
            thirdy_party_login=True,
            thirdy_party_login_name='Personal Main Account',
            login='-----',
            password='-----',
        )

    def test_credential_instance_validity(self):
        """Tests if setUp's credentials are correctly instancied"""

        cred1 = LoginCredential.objects.get(pk=1)
        cred2 = LoginCredential.objects.get(pk=2)
        cred3 = LoginCredential.objects.get(pk=3)
        cred4 = LoginCredential.objects.get(pk=4)
        cred5 = LoginCredential.objects.get(pk=5)
        cred6 = LoginCredential.objects.get(pk=6)
        cred7 = LoginCredential.objects.get(pk=7)

        self.assertIsInstance(cred1, LoginCredential)
        self.assertIsInstance(cred2, LoginCredential)
        self.assertIsInstance(cred3, LoginCredential)
        self.assertIsInstance(cred4, LoginCredential)
        self.assertIsInstance(cred5, LoginCredential)
        self.assertIsInstance(cred6, LoginCredential)
        self.assertIsInstance(cred7, LoginCredential)

    def test_credential_key_value_assertion(self):
        """Tests if keys and values are properly assigned"""

        cred1 = LoginCredential.objects.get(pk=1)

        self.assertEqual(cred1.service, 'google-')
        self.assertEqual(cred1.name, 'Personal Main Account')
        self.assertEqual(cred1.slug, 'google--personal-main-account')
        self.assertFalse(cred1.thirdy_party_login)
        self.assertEqual(cred1.thirdy_party_login_name, '-----')
        self.assertEqual(cred1.login, 'night_monkey123@gmail.com')
        self.assertEqual(cred1.password, 'ilovemenotyou')

    def test_credential_user_foreign_key_validity(self):
        """Tests credential.owner is properly assigned"""

        cred1 = LoginCredential.objects.get(pk=1)
        cred2 = LoginCredential.objects.get(pk=2)

        cred1_owner = cred1.owner
        cred2_owner = cred2.owner

        user = User.objects.get(pk=1)

        self.assertEqual(cred1_owner, cred2_owner)
        self.assertEqual(cred1_owner, user)

    def test_credential_create_validity(self):
        """Tests if created credentials are valid or not"""

        cred1 = LoginCredential.objects.get(pk=1)
        cred2 = LoginCredential.objects.get(pk=2)
        cred3 = LoginCredential.objects.get(pk=3)
        cred4 = LoginCredential.objects.get(pk=4)
        cred5 = LoginCredential.objects.get(pk=5)
        cred6 = LoginCredential.objects.get(pk=6)
        cred7 = LoginCredential.objects.get(pk=7)

        self.assertEqual(LoginCredential.objects.all().count(), 7)

        self.assertTrue(cred1.is_valid())
        self.assertTrue(cred2.is_valid())
        self.assertFalse(cred3.is_valid())
        self.assertFalse(cred4.is_valid())
        self.assertFalse(cred5.is_valid())
        self.assertFalse(cred6.is_valid())
        self.assertFalse(cred7.is_valid())

    def test_credential_update_validity(self):
        """Tests if updated credentials are valid or not"""

        cred1 = LoginCredential.objects.get(pk=1)
        cred2 = LoginCredential.objects.get(pk=2)
        cred3 = LoginCredential.objects.get(pk=3)
        cred4 = LoginCredential.objects.get(pk=4)
        cred5 = LoginCredential.objects.get(pk=5)
        cred6 = LoginCredential.objects.get(pk=6)
        cred7 = LoginCredential.objects.get(pk=7)

        cred1.service = ''
        cred2.slug = 'diners-club-international--tupinamba'
        cred3.thirdy_party_login = False
        cred4.slug = 'steam--little-fries'
        cred4.login = 'some_login_text_or_email_or_some_other_stuff_like_this'
        cred5.password = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        cred6.name = 'Personal Main Account'
        cred6.login = 'bananinha_assada_3_2_1'
        cred7.service = 'visa-'
        cred7.slug = 'visa--little-fries'

        cred1.save()
        cred2.save()
        cred3.save()
        cred4.save()
        cred5.save()
        cred6.save()
        cred7.save()

        self.assertFalse(cred1.is_valid())
        self.assertFalse(cred2.is_valid())
        self.assertTrue(cred3.is_valid())
        self.assertTrue(cred4.is_valid())
        self.assertTrue(cred5.is_valid())
        self.assertTrue(cred6.is_valid())
        self.assertTrue(cred7.is_valid())

    def test_credential_delete_validity(self):
        """Tests if objects are correctly deleted or not"""

        cred1 = LoginCredential.objects.get(pk=1)
        cred2 = LoginCredential.objects.get(pk=2)
        cred3 = LoginCredential.objects.get(pk=3)
        cred4 = LoginCredential.objects.get(pk=4)
        cred5 = LoginCredential.objects.get(pk=5)
        cred6 = LoginCredential.objects.get(pk=6)
        cred7 = LoginCredential.objects.get(pk=7)
        
        cred3.delete()
        cred4.delete()
        cred5.delete()
        cred6.delete()
        cred7.delete()

        self.assertEqual(LoginCredential.objects.all().count(), 2)

        self.assertTrue(cred1.is_valid())
        self.assertTrue(cred2.is_valid())


class CardTestCase(TestCase):
    def test_stuff(self):
        test_user = User.objects.create(
            username='test_user',
            password='testing_password',
            email='test@email.com',
            first_name='Test',
            last_name='User'
        )

        Card.objects.create(
            owner=test_user,
            name='Personal Main Card',
            card_type='Débito',
            number='4002892240028922',
            expiration=Month(2028, 11),
            cvv=113,
            bank='nubank-',
            brand='mastercard-',
            slug='nubank--personal-main-card',
            owners_name='TEST USER',
        )  # Correct object

        Card.objects.create(
            owner=test_user,
            name='Personal Main Card',
            card_type='Crediário',  # Wrong type
            number='4002892240028922',
            expiration=Month(2028, 11),
            cvv=113,
            bank='nubank-',
            brand='mastercard-',
            slug='nubank--personal-main-card',
            owners_name='TEST USER',
        )

        Card.objects.create(
            owner=test_user,
            name='Personal Main Card',
            card_type='Débito',
            number='123456789',  # Length out of range
            expiration=Month(2028, 11),
            cvv=12345,  # Length out of range
            bank='nubank-',
            brand='mastercard-',
            slug='nubank--personal-main-card',
            owners_name='TEST USER',
        )

        Card.objects.create(
            owner=test_user,
            name='Personal Main Card',
            card_type='Débito',
            number='4002892240028922',
            expiration=Month(2028, 11),
            cvv=113,
            bank='mingau-',  # Inexistent service
            brand='mastercard-',
            slug='mingau--personal-main-card',
            owners_name='TEST USER',
        )

        Card.objects.create(
            owner=test_user,
            name='Personal Main Card',
            card_type='Débito',
            number='4002892240028922',
            expiration=Month(2028, 11),
            cvv=113,
            bank='nubank-',
            brand='mastercard-',
            slug='nubank--minotauro',  # Should be 'nubank--personal-main-card'
            owners_name='TEST USER',
        )