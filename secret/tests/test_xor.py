from django.test import TestCase
from faker import Faker

from account.models import User
from secret.xor_db import xor


class XORTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(
            username='test_user',
            password='testing_password',
            email='test@email.com',
            first_name='Test',
            last_name='User'
        )

        self.f = Faker()

    def test_xor_null_value(self):
        """Tests if xor() retuns a NULL (\x00) value"""

        UNIVERSE = 100000
        password = User.objects.get(pk=1).password
        
        encrypted_usernames = [xor(self.f.simple_profile()['username'], password[21:]) for _ in range(UNIVERSE)]
        encrypted_mails = [xor(self.f.simple_profile()['mail'], password[21:]) for _ in range(UNIVERSE)]

        decrypted_usernames = [xor(username, password[21:], encrypt=False) for username in encrypted_usernames]
        decrypted_mails = [xor(mail, password[21:], encrypt=False) for mail in encrypted_mails]


        for username, mail in list(zip(encrypted_usernames, encrypted_mails)):
            self.assertNotIn('\x00', username)
            self.assertTrue(all(map(lambda x: x in range(0x110000), [ord(i) for i in username])))

            self.assertNotIn('\x00', mail)
            self.assertTrue(all(map(lambda x: x in range(0x110000), [ord(i) for i in mail])))


        for username, mail in list(zip(decrypted_usernames, decrypted_mails)):
            self.assertNotIn('\x00', username)
            self.assertTrue(all(map(lambda x: x in range(0x110000), [ord(i) for i in username])))

            self.assertNotIn('\x00', mail)
            self.assertTrue(all(map(lambda x: x in range(0x110000), [ord(i) for i in mail])))
