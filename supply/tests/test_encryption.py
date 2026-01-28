"""
    Here are the unit tests for encryption and
    descryption of phone from registered suppliers.
"""

from django.test import TestCase

from supply.models import Supplier


class SupplierEncryptionTestCase(TestCase):

    def test_encryption_phone(self):
        phone = "(41) 99999-9999"
        encrypted = Supplier.encrypt_phone(phone)

        self.assertNotEquals(encrypted, phone)
        self.assertTrue(encrypted.startswith("gAAAA"))

    def test_decryption_phone(self):
        phone = "(41) 99999-9999"

        encrypted = Supplier.encrypt_phone(phone)
        decrypted = Supplier.decrypt_phone(encrypted)

        self.assertEqual(decrypted, phone)
