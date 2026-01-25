from django.db import models
from django.conf import settings

from uuid import uuid4
from cryptography.fernet import Fernet, InvalidToken
import base64
import hashlib

class Fornecedor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    telefone = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    @staticmethod
    def get_encryption_key():
        key = hashlib.sha256(settings.SECRET_KEY.encode()).digest()

        return base64.urlsafe_b64encode(key)

    @staticmethod
    def encrypt_phone(phone: str) -> str:

        if not phone:
            return ''

        fernet = Fernet(Fornecedor.get_encryption_key())
        encrypted = fernet.encrypt(phone.encode())

        return encrypted.decode()

    @staticmethod
    def decrypt_phone(encrypted_phone: str) -> str:
        if not encrypted_phone:
            return ''

        try:
            fernet = Fernet(Fornecedor.get_encryption_key())
            decrypted = fernet.decrypt(encrypted_phone.encode())

            return decrypted.decode()
        except InvalidToken:
            return encrypted_phone

    def save(self, *args, **kwargs):

        if self.telefone and not self.telefone.startswith('gAAAA'):
            self.telefone = self.encrypt_phone(self.telefone)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
