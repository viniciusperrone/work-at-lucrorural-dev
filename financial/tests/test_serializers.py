"""
    Here is the validation of the Serializer from
    same supplier.
"""

from django.test import TestCase
from rest_framework.serializers import ValidationError
from decimal import Decimal

from supply.models import Supplier
from contabil.models import Invoice
from financial.models import AccountPayable
from financial.serializers import AccountPayableSerializer


class AccountPayableSerializerTestCase(TestCase):

    def setUp(self):
        """Create test data"""
        self.supplier1 = Supplier.objects.create(
            name="Supplier 1",
            cnpj="12345678000190",
            phone="(41) 99999-8888"
        )

        self.supplier2 = Supplier.objects.create(
            name="Supplier 2",
            cnpj="98765432000110",
            phone="(41) 98888-7777"
        )

        self.invoice1 = Invoice.objects.create(
            invoice_number=1001,
            supplier=self.supplier1,
            product_name="Product 1",
            product_category="Category A",
            quantity=Decimal("10.00"),
            total_amount=Decimal("500.00")
        )

        self.invoice2 = Invoice.objects.create(
            invoice_number=1002,
            supplier=self.supplier1,
            product_name="Product 2",
            product_category="Category A",
            quantity=Decimal("5.00"),
            total_amount=Decimal("250.00")
        )

        self.invoice3 = Invoice.objects.create(
            invoice_number=2001,
            supplier=self.supplier2,
            product_name="Product 3",
            product_category="Category B",
            quantity=Decimal("20.00"),
            total_amount=Decimal("1000.00")
        )

    def test_create_account_payable_with_same_supplier_invoices(self):
        """Test creating account payable with invoices from same supplier - should succeed"""
        data = {
            'supplier': self.supplier1.id,
            'deadline': '2025-02-15',
            'is_paid': False,
            'invoices': [self.invoice1.id, self.invoice2.id]
        }

        serializer = AccountPayableSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        account_payable = serializer.save()
        account_payable.invoices.set(data['invoices'])

        self.assertEqual(account_payable.invoices.count(), 2)

    def test_create_account_payable_with_different_supplier_invoices(self):
        """Test creating account payable with invoices from different suppliers - should fail"""
        data = {
            'supplier': self.supplier1.id,
            'deadline': '2025-02-15',
            'is_paid': False,
            'invoices': [self.invoice1.id, self.invoice3.id]
        }

        serializer = AccountPayableSerializer(data=data)

        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
