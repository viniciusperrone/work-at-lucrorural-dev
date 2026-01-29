"""
    Test Data Filtering
"""
from uuid import UUID
from datetime import date

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from supply.models import Supplier
from financial.models import AccountPayable


class AccountPayableFilterTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.view_name = "financial-account-payable-list"

        self.supplier = Supplier.objects.create(
            name="Joao da Silva",
            cnpj="03560714000142",
            phone="41999998888"
        )

        self.account_payable1 = AccountPayable.objects.create(
            supplier=self.supplier,
            deadline=date(2022, 1, 1),
            is_paid=False
        )

        self.account_payable2 = AccountPayable.objects.create(
            supplier=self.supplier,
            deadline=date(2022, 2, 1),
            is_paid=False
        )

        self.account_payable3 = AccountPayable.objects.create(
            supplier=self.supplier,
            deadline=date(2022, 3, 1),
            is_paid=False
        )

    def test_filter_by_deadline_start(self):
        url = reverse(self.view_name)
        response = self.client.get(url, {'deadline_start': '2022-02-01'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_by_deadline_end(self):
        url = reverse(self.view_name)
        response = self.client.get(url, {'deadline_end': '2022-02-27'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_by_date_range(self):
        url = reverse(self.view_name)
        response = self.client.get(url, {
            'deadline_start': '2022-02-01',
            'deadline_end': '2022-02-28'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(UUID(response.data[0]['id']), self.account_payable2.id)

    def test_filter_by_supplier_name(self):
        supplier = Supplier.objects.create(
            name="Joao da Silva",
            cnpj="03560714000142",
            phone="41999998888"
        )

        AccountPayable.objects.create(
            supplier=supplier,
            deadline=date(2025, 1, 20),
            is_paid=False
        )

        url = reverse(self.view_name)
        response = self.client.get(url, {'supplier_name': 'Joao'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_filter_combined(self):
        url = reverse(self.view_name)
        response = self.client.get(url, {
            'deadline_start': '2022-01-01',
            'deadline_end': '2022-12-31',
            'supplier_name': 'Joao'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
