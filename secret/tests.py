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
        """Tests if credential's keys and values are properly assigned"""

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

        LoginCredential.objects.filter(pk=1).update(service='')
        LoginCredential.objects.filter(pk=2).update(slug='diners-club-international--tupinamba')
        LoginCredential.objects.filter(pk=3).update(thirdy_party_login=False)
        LoginCredential.objects.filter(pk=4).update(slug='steam--little-fries', login='some_login_text_or_email_or_some_other_stuff_like_this')
        LoginCredential.objects.filter(pk=5).update(password='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        LoginCredential.objects.filter(pk=6).update(name='Personal Main Account', login='bananinha_assada_3_2_1')
        LoginCredential.objects.filter(pk=7).update(service='visa-', slug='visa--little-fries')

        cred1 = LoginCredential.objects.get(pk=1)
        cred2 = LoginCredential.objects.get(pk=2)
        cred3 = LoginCredential.objects.get(pk=3)
        cred4 = LoginCredential.objects.get(pk=4)
        cred5 = LoginCredential.objects.get(pk=5)
        cred6 = LoginCredential.objects.get(pk=6)
        cred7 = LoginCredential.objects.get(pk=7)

        self.assertFalse(cred1.is_valid())
        self.assertFalse(cred2.is_valid())
        self.assertTrue(cred3.is_valid())
        self.assertTrue(cred4.is_valid())
        self.assertTrue(cred5.is_valid())
        self.assertTrue(cred6.is_valid())
        self.assertTrue(cred7.is_valid())

    def test_credential_delete_validity(self):
        """Tests if credential objects are correctly deleted or not"""

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
    def setUp(self):
        test_user = User.objects.create(
            username='test_user',
            password='testing_password',
            email='test@email.com',
            first_name='Test',
            last_name='User'
        )

        # Object 1
        Card.objects.create(
            owner=test_user,
            name='Personal Main Card',
            card_type='Débito',
            number='4002892240028922',
            expiration=Month(2028, 11),
            cvv='113',
            bank='nubank-',
            brand='mastercard-',
            slug='nubank--personal-main-card',
            owners_name='TEST USER',
        )  # Correct object

        # Object 2
        Card.objects.create(
            owner=test_user,
            name='Personal Main Card',
            card_type='Crediário',  # Inexintent type
            number='4002892240028922',
            expiration=Month(2028, 11),
            cvv=113,
            bank='nubank-',
            brand='mastercard-',
            slug='nubank--personal-main-card',
            owners_name='TEST USER',
        )

        # Object 3
        Card.objects.create(
            owner=test_user,
            name='Personal Main Card',
            card_type='Débito',
            number='123456789',  # Length out of range
            expiration=Month(2028, 11),
            cvv=12,  # Length out of range
            bank='nubank-',
            brand='mastercard-',
            slug='nubank--personal-main-card',
            owners_name='TEST USER',
        )

        # Object 4
        Card.objects.create(
            owner=test_user,
            name='Personal Main Card',
            card_type='Débito',
            number='4002892240028922',
            expiration=Month(2028, 11),
            cvv=113,
            bank='mingau-',  # Inexistent bank
            brand='mastercard-',
            slug='mingau--personal-main-card',
            owners_name='TEST USER',
        )

        # Object 5
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

        # Object 6
        Card.objects.create(
            owner=test_user,
            name='Personal Main Card',
            card_type='Débito',
            number='4002892240028922',
            expiration='2023/4',
            cvv=113,
            bank='nubank-',
            brand='vina-',  # Inexistent brand
            slug='nubank--personal-main-card',
            owners_name='TEST USER',
        )

    def test_card_instance_validity(self):
        """Tests if setUp's cards are correctly instancied"""

        card1 = Card.objects.get(pk=1)
        card2 = Card.objects.get(pk=2)
        card3 = Card.objects.get(pk=3)
        card4 = Card.objects.get(pk=4)
        card5 = Card.objects.get(pk=5)
        card6 = Card.objects.get(pk=6)

        self.assertIsInstance(card1, Card)
        self.assertIsInstance(card2, Card)
        self.assertIsInstance(card3, Card)
        self.assertIsInstance(card4, Card)
        self.assertIsInstance(card5, Card)
        self.assertIsInstance(card6, Card)

    def test_card_key_value_assertion(self):
        """Tests if card's keys and values are properly assigned"""

        card1 = Card.objects.get(pk=1)

        self.assertEqual(card1.name, 'Personal Main Card')
        self.assertEqual(card1.card_type, 'Débito')
        self.assertEqual(card1.number, '4002892240028922')
        self.assertEqual(card1.expiration, Month(2028, 11))
        self.assertEqual(card1.cvv, '113')
        self.assertEqual(card1.bank, 'nubank-')
        self.assertEqual(card1.brand, 'mastercard-')
        self.assertEqual(card1.slug, 'nubank--personal-main-card')
        self.assertEqual(card1.owners_name, 'TEST USER')

    def test_card_user_foreign_key_validity(self):
        """Tests card.owner is properly assigned"""

        card1 = Card.objects.get(pk=1)
        user = User.objects.get(pk=1)

        self.assertEqual(card1.owner, user)

    def test_card_create_validity(self):
        """Tests if created cards are valid or not"""

        card1 = Card.objects.get(pk=1)
        card2 = Card.objects.get(pk=2)
        card3 = Card.objects.get(pk=3)
        card4 = Card.objects.get(pk=4)
        card5 = Card.objects.get(pk=5)
        card6 = Card.objects.get(pk=6)

        self.assertEqual(Card.objects.all().count(), 6)

        self.assertTrue(card1.is_valid())
        self.assertFalse(card2.is_valid())
        self.assertFalse(card3.is_valid())
        self.assertFalse(card4.is_valid())
        self.assertFalse(card5.is_valid())
        self.assertFalse(card6.is_valid())

    def test_card_update_validity(self):
        """Tests if updated cards are valid or not"""

        Card.objects.filter(pk=1).update(cvv='14000605')
        Card.objects.filter(pk=2).update(card_type='Débito')
        Card.objects.filter(pk=3).update(number='1122334455667788', cvv='1986')
        Card.objects.filter(pk=4).update(bank='pagseguro-', slug='pagseguro--personal-main-card')
        Card.objects.filter(pk=5).update(slug='nubank--personal-main-card')
        Card.objects.filter(pk=6).update(brand='mastercard-')

        card1 = Card.objects.get(pk=1)
        card2 = Card.objects.get(pk=2)
        card3 = Card.objects.get(pk=3)
        card4 = Card.objects.get(pk=4)
        card5 = Card.objects.get(pk=5)
        card6 = Card.objects.get(pk=6)

        self.assertFalse(card1.is_valid())
        self.assertTrue(card2.is_valid())
        self.assertTrue(card3.is_valid())
        self.assertTrue(card4.is_valid())
        self.assertTrue(card5.is_valid())
        self.assertTrue(card6.is_valid())

    def test_card_delete_validity(self):
        """Tests if card objects are correctly deleted or not"""

        card1 = Card.objects.get(pk=1)
        card2 = Card.objects.get(pk=2)
        card3 = Card.objects.get(pk=3)
        card4 = Card.objects.get(pk=4)
        card5 = Card.objects.get(pk=5)
        card6 = Card.objects.get(pk=6)
        
        card2.delete()
        card3.delete()
        card4.delete()
        card5.delete()
        card6.delete()

        self.assertEqual(Card.objects.all().count(), 1)

        self.assertTrue(card1.is_valid())
