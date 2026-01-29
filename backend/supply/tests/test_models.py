"""
    Here there Test CNPJ Formatting
"""
from django.test import TestCase
from utils.cnpj import format_cnpj_safe

from supply.models import Supplier


class SupplierCNPJFormattingTestCase(TestCase):

    def setUp(self):
        self.cnpj_raw = "03560714000142"
        self.cnpj_formatted = "03.560.714/0001-42"

    def test_cnpj_formatting(self):
        formatted = format_cnpj_safe(self.cnpj_raw)

        self.assertEqual(formatted, self.cnpj_formatted)

    def test_supplier_cnpj_stored_unformatted(self):
        """Test that CNPJ is stored unformatted in database"""
        supplier = Supplier.objects.create(
            name="Joao da Silva",
            cnpj="03560714000142",
            phone="41999998888"
        )

        self.assertEqual(supplier.cnpj, self.cnpj_raw)

        formatted = format_cnpj_safe(supplier.cnpj)
        self.assertEqual(formatted, self.cnpj_formatted)
