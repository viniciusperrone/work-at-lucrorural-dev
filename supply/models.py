from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from uuid import uuid4
from cryptography.fernet import Fernet, InvalidToken
import base64
import hashlib

class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name=_('Nome'))
    cnpj = models.CharField(max_length=18, verbose_name=_('CNPJ'))
    phone = models.CharField(max_length=255, verbose_name=_('Telefone'))

    class Meta:
        verbose_name = _('Fornecedor')
        verbose_name_plural = _('Fornecedores')

    @staticmethod
    def get_encryption_key():
        key = hashlib.sha256(settings.SECRET_KEY.encode()).digest()

        return base64.urlsafe_b64encode(key)

    @staticmethod
    def encrypt_phone(phone: str) -> str:

        if not phone:
            return ''

        fernet = Fernet(Supplier.get_encryption_key())
        encrypted = fernet.encrypt(phone.encode())

        return encrypted.decode()

    @staticmethod
    def decrypt_phone(encrypted_phone: str) -> str:
        if not encrypted_phone:
            return ''

        try:
            fernet = Fernet(Supplier.get_encryption_key())
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
