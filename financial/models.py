import uuid

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import Sum


class AccountPayable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    supply = models.ForeignKey('supply.Supplier', related_name='account_payable', on_delete=models.PROTECT, verbose_name=_('Fornecedor'))
    deadline = models.DateField(verbose_name=_('Data de Vencimento'))
    is_paid = models.BooleanField(default=False, verbose_name=_('Pago'))
    invoices = models.ManyToManyField('contabil.PurchaseInvoiceItems', related_name='account_payable', blank=True, verbose_name=_('Notas Fiscais'))

    def clean(self):
        super().clean()

        if self.pk:
            invoices = self.invoices.all()

            if invoices.exists():
                invalid_invoices = invoices.exclude(supplier=self.supply)

                if invalid_invoices.exists():
                    raise ValidationError({
                        'invoices': _('Todas as notas fiscais devem pertencer ao mesmo fornecedor ')
                    })


    def delete(self, *args, **kwargs):
        if self.invoices.exists():
            raise ValidationError('Cannot delete multiple. There are linked invoices.')

        super().delete(*args, **kwargs)

    @property
    def total_amount(self):
        return self.invoices.aggregate(total=Sum('total_amount'))['total'] or 0.0
