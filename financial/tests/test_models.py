"""
    Test Total Amount Calculation
"""
from decimal import Decimal

from django.test import TestCase

from supply.models import Supplier
from financial.models import AccountPayable
from contabil.models import Invoice


class AccountPayableTotalAmountTestCase(TestCase):

    def setUp(self):
        self.supplier = Supplier.objects.create(
            name="Joao da Silva",
            cnpj="03560714000142",
            phone="41999998888"
        )

        self.invoice1 = Invoice.objects.create(
            invoice_number=1001,
            supplier=self.supplier,
            product_name="Product 1",
            quantity=Decimal("10.0"),
            total_amount=Decimal("50.00")
        )
        self.invoice2 = Invoice.objects.create(
            invoice_number=1002,
            supplier=self.supplier,
            product_name="Product 2",
            quantity=Decimal("5.0"),
            total_amount=Decimal("250.00")
        )

    def test_total_amount_with_no_invoices(self):
        """Test total amount no invoices are linked"""
        account_payable = AccountPayable.objects.create(
            supplier=self.supplier,
            deadline='2025-01-26',
            is_paid=True
        )

        self.assertEqual(account_payable.total_amount, 0.0)

    def test_total_amount_with_single_invoice(self):
        """Test total amount with single invoice is linked"""
        account_payable = AccountPayable.objects.create(
            supplier=self.supplier,
            deadline='2025-01-26',
            is_paid=True
        )

        account_payable.invoices.add(self.invoice1)

        self.assertEqual(account_payable.total_amount, Decimal("50.00"))

    def test_total_amount_with_multiple_invoices(self):
        """Test total amount with multiple invoices are linked"""
        account_payable = AccountPayable.objects.create(
            supplier=self.supplier,
            deadline='2025-01-26',
            is_paid=True
        )

        account_payable.invoices.add(self.invoice1, self.invoice2)

        expected_amount = Decimal("50.00") + Decimal("250.00")
        self.assertEqual(account_payable.total_amount, expected_amount)

    def test_total_amount_updated_when_invoices_change(self):
        """Test total amount updated when invoices change"""
        account_payable = AccountPayable.objects.create(
            supplier=self.supplier,
            deadline='2025-01-26',
            is_paid=False
        )

        self.assertEqual(account_payable.total_amount, 0.0)

        account_payable.invoices.add(self.invoice1)
        self.assertEqual(account_payable.total_amount, Decimal("50.00"))

        account_payable.invoices.add(self.invoice2)
        expected_amount = Decimal("50.00") + Decimal("250.00")

        self.assertEqual(account_payable.total_amount, expected_amount)

        account_payable.invoices.remove(self.invoice1)
        self.assertEqual(account_payable.total_amount, Decimal("250.00"))
