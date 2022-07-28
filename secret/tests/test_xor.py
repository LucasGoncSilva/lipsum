import queue
import threading

from django.test import TestCase
from faker import Faker

from account.models import User
from secret.xor_db import xor


class XORTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(
            username='test_user',
            password='testing_password',
            email='test_user@example.com',
            first_name='Test',
            last_name='User'
        )

        self.f = Faker()
        self.q_encrypted = queue.Queue()
        self.q_decrypted = queue.Queue()
        self.num = 100_000
        self.password = User.objects.get(pk=1).password

    def test_xor_null_value(self):
        """Tests if xor() retuns a NULL (\x00) value"""

        for _ in range(self.num):
            encrypted_username = xor(self.f.simple_profile()['username'], self.password[21:])
            encrypted_mail = xor(self.f.simple_profile()['mail'], self.password[21:])

            decrypted_username = xor(encrypted_username, self.password[21:], encrypt=False)
            decrypted_mail = xor(encrypted_mail, self.password[21:], encrypt=False)

            self.q_encrypted.put((encrypted_username, encrypted_mail))
            self.q_decrypted.put((decrypted_username, decrypted_mail))

        threading.Thread(target=self.xor_null_value_in_encryptation, daemon=True).start()
        self.q_encrypted.join()

        threading.Thread(target=self.xor_null_value_in_decryptation, daemon=True).start()
        self.q_decrypted.join()

    def xor_null_value_in_encryptation(self):
        while True:
            username, mail = self.q_encrypted.get()

            self.assertNotIn('\x00', username)
            self.assertTrue(all(map(lambda x: x in range(0x110000), [ord(i) for i in username])))

            self.assertNotIn('\x00', mail)
            self.assertTrue(all(map(lambda x: x in range(0x110000), [ord(i) for i in mail])))

            self.q_encrypted.task_done()

    def xor_null_value_in_decryptation(self):
        while True:
            username, mail = self.q_decrypted.get()

            self.assertNotIn('\x00', username)
            self.assertTrue(all(map(lambda x: x in range(0x110000), [ord(i) for i in username])))

            self.assertNotIn('\x00', mail)
            self.assertTrue(all(map(lambda x: x in range(0x110000), [ord(i) for i in mail])))

            self.q_decrypted.task_done()
