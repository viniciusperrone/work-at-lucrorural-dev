from django.db import models

from uuid import uuid4


class Fornecedor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    telefone = models.CharField(min_length= 10, max_length=11)