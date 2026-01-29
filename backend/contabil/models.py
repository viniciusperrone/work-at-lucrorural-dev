import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice_number = models.IntegerField(verbose_name=_('Número da nota fiscal'))
    supplier = models.ForeignKey('supply.Supplier', on_delete=models.CASCADE, verbose_name=_('Fornecedor'))
    issue_date = models.DateField(default=timezone.now, verbose_name=_('Data de emissão'))
    product_name = models.CharField(max_length=255, verbose_name=_('Nome do produto'))
    product_category = models.CharField(max_length=255, verbose_name=_('Categoria do produto'))
    quantity = models.DecimalField(default=0.0, decimal_places=2, max_digits=10, verbose_name=_('Quantidade'))
    total_amount = models.DecimalField(default=0.0, decimal_places=2, max_digits=10, verbose_name=_('Valor total'))

    class Meta:
        verbose_name = _('Item da nota fiscal de compra')
        verbose_name_plural = _('Itens da nota fiscal de compra')

    def __str__(self):
        return f"{self.invoice_number} - {self.product_name}"
