import uuid

from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import Sum


class AccountPayable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    supplier = models.ForeignKey('supply.Supplier', related_name='account_payable', on_delete=models.PROTECT, verbose_name=_('Fornecedor'))
    deadline = models.DateField(verbose_name=_('Data de Vencimento'))
    is_paid = models.BooleanField(default=False, verbose_name=_('Pago'))
    invoices = models.ManyToManyField('contabil.Invoice', related_name='account_payable', blank=True, verbose_name=_('Notas Fiscais'))


    @property
    def total_amount(self):
        return self.invoices.aggregate(total=Sum('total_amount'))['total'] or 0.0
