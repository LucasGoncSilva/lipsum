from django.test import TestCase

from accounts.models import User
from .models import Card, LoginCredential, SecurityNote
from .month.models import Month
from .encript_db import cover, uncover


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

        # Object 1
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

        # Object 2
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

        # Object 3
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

        # Object 4
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

        # Object 5
        LoginCredential.objects.create(
            owner=test_user,
            service='steam-',
            name='Little Fries',
            slug='steam--little-fries',
            thirdy_party_login=False,
            thirdy_party_login_name='-----',
            login='night_monkey123',
            # Missing/empty password field
        )

        # Object 6
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

        # Object 7
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
        """Tests if credential.owner is properly assigned"""

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
            card_type='deb',
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
            card_type='creda',  # Inexintent type
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
            card_type='deb',
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
            card_type='deb',
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
            card_type='deb',
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
            card_type='deb',
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
        self.assertEqual(card1.card_type, 'deb')
        self.assertEqual(card1.number, '4002892240028922')
        self.assertEqual(card1.expiration, Month(2028, 11))
        self.assertEqual(card1.cvv, '113')
        self.assertEqual(card1.bank, 'nubank-')
        self.assertEqual(card1.brand, 'mastercard-')
        self.assertEqual(card1.slug, 'nubank--personal-main-card')
        self.assertEqual(card1.owners_name, 'TEST USER')

    def test_card_user_foreign_key_validity(self):
        """Tests if card.owner is properly assigned"""

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

        user = User.objects.get(pk=1)

        Card.objects.filter(pk=1).update(cvv=cover('14000605', user.password))
        Card.objects.filter(pk=2).update(card_type=cover('deb', user.password))
        Card.objects.filter(pk=3).update(
            number=cover('1122334455667788', user.password),
            cvv=cover('1986', user.password)
        )
        Card.objects.filter(pk=4).update(
            bank=cover('pagseguro-', user.password),
            slug='pagseguro--personal-main-card'
        )
        Card.objects.filter(pk=5).update(slug='nubank--personal-main-card')
        Card.objects.filter(pk=6).update(brand=cover('mastercard-', user.password))

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


class SecurityNoteTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create(
            username='test_user',
            password='testing_password',
            email='test@email.com',
            first_name='Test',
            last_name='User'
        )

        # Object 1
        SecurityNote.objects.create(
            owner=test_user,
            title='How to draw an apple',
            slug='how-to-draw-an-apple',
            content='Just draw an apple tree and erase the tree.'
        )  # Correct object

        # Object 2
        SecurityNote.objects.create(
            owner=test_user,
            title='How to draw a tree',
            slug='howtodrawatree',  # Should be 'how-to-draw-a-tree'
            content='Just draw an apple tree and erase the apples.'
        )

        # Object 3
        SecurityNote.objects.create(
            owner=test_user,
            title='How to draw an apple tree',
            slug='how-to-draw-an-apple-tree',
            content='x'*333  # Length out of range
        )

        # Object 4
        SecurityNote.objects.create(
            owner=test_user,
            title='How to draw an apple tree leaf',
            slug='how-to-draw-an-apple-tree-leaf',
        )  # Missing/empty content field

    def test_note_instance_validity(self):
        """Tests if setUp's notes are correctly instancied"""

        note1 = SecurityNote.objects.get(pk=1)
        note2 = SecurityNote.objects.get(pk=2)
        note3 = SecurityNote.objects.get(pk=3)
        note4 = SecurityNote.objects.get(pk=4)

        self.assertIsInstance(note1, SecurityNote)
        self.assertIsInstance(note2, SecurityNote)
        self.assertIsInstance(note3, SecurityNote)
        self.assertIsInstance(note4, SecurityNote)

    def test_note_key_value_assertion(self):
        """Tests if note's keys and values are properly assigned"""

        note1 = SecurityNote.objects.get(pk=1)

        self.assertEqual(note1.title, 'How to draw an apple')
        self.assertEqual(note1.slug, 'how-to-draw-an-apple')
        self.assertEqual(note1.content, 'Just draw an apple tree and erase the tree.')

    def test_note_user_foreign_key_validity(self):
        """Tests if note.owner is properly assigned"""

        note1 = SecurityNote.objects.get(pk=1)
        user = User.objects.get(pk=1)

        self.assertEqual(note1.owner, user)

    def test_note_create_validity(self):
        """Tests if created notes are valid or not"""

        note1 = SecurityNote.objects.get(pk=1)
        note2 = SecurityNote.objects.get(pk=2)
        note3 = SecurityNote.objects.get(pk=3)
        note4 = SecurityNote.objects.get(pk=4)

        self.assertEqual(SecurityNote.objects.all().count(), 4)

        self.assertTrue(note1.is_valid())
        self.assertFalse(note2.is_valid())
        self.assertFalse(note3.is_valid())
        self.assertFalse(note4.is_valid())

    def test_note_update_validity(self):
        """Tests if updated notes are valid or not"""

        SecurityNote.objects.filter(pk=1).update(title='How not to draw an apple')
        SecurityNote.objects.filter(pk=2).update(slug='how-to-draw-a-tree')
        SecurityNote.objects.filter(pk=3).update(content='Draw a tree and then the apples.')
        SecurityNote.objects.filter(pk=4).update(content='Draw an apple tree and then erase the apples and the tree.')

        note1 = SecurityNote.objects.get(pk=1)
        note2 = SecurityNote.objects.get(pk=2)
        note3 = SecurityNote.objects.get(pk=3)
        note4 = SecurityNote.objects.get(pk=4)

        self.assertFalse(note1.is_valid())
        self.assertTrue(note2.is_valid())
        self.assertTrue(note3.is_valid())
        self.assertTrue(note4.is_valid())

    def test_note_delete_validity(self):
        """Tests if note objects are correctly deleted or not"""

        note1 = SecurityNote.objects.get(pk=1)
        note2 = SecurityNote.objects.get(pk=2)
        note3 = SecurityNote.objects.get(pk=3)
        note4 = SecurityNote.objects.get(pk=4)
        
        note2.delete()
        note3.delete()
        note4.delete()

        self.assertEqual(SecurityNote.objects.all().count(), 1)

        self.assertTrue(note1.is_valid())
