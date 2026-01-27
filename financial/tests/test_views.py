"""
    Here there Test Business Rule: Cannot Delete with
    linked invoices
"""
from decimal import Decimal

from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from financial.models import AccountPayable
from supply.models import Supplier
from contabil.models import Invoice


class AccountPayableDeleteTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.supplier = Supplier.objects.create(
            name="Test Supplier",
            cnpj="12345678000190",
            phone="(41) 99999-8888"
        )

        self.invoice = Invoice.objects.create(
            invoice_number=1001,
            supplier=self.supplier,
            product_name="Product 1",
            product_category="Category A",
            quantity=Decimal("10.00"),
            total_amount=Decimal("500.00")
        )

    def test_delete_account_payable_without_invoice(self):
        """Test deleting account payable without linked invoice - should succeed"""
        account_payable = AccountPayable.objects.create(
            supplier=self.supplier,
            deadline='2025-02-15',
            is_paid=False
        )

        url = reverse('financial-account-payable-retrieve-destroy', kwargs={'id': account_payable.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(AccountPayable.objects.filter(pk=account_payable.id).exists())

    def test_delete_account_payable_with_invoice(self):
        """Test deleting account payable with linked invoice - should succeed"""
        account_payable = AccountPayable.objects.create(
            supplier=self.supplier,
            deadline='2025-02-15',
            is_paid=False
        )

        account_payable.invoices.add(self.invoice)

        url = reverse('financial-account-payable-retrieve-destroy', kwargs={'id': account_payable.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(AccountPayable.objects.filter(pk=account_payable.id).exists())
        self.assertIn('detail', response.data)