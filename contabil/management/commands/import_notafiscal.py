import csv
import os
from datetime import datetime as dt

from django.core.management import BaseCommand
from django.conf import settings

from contabil.models import PurchaseInvoiceItems
from supply.models import Fornecedor

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'csv_file',
            type=str,
            nargs='?',
            default='contabil/fixtures/notafiscal.csv',
            help='CSV file path relative to BASE_DIR'
        )

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        csv_path = os.path.join(settings.BASE_DIR, csv_file)

        try:
            with open(csv_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';')

                for row in reader:
                    invoice_number = row['numero_nota'].strip()
                    supplier_id = row['fornecedor'].strip()
                    issue_date = row['data_emissao'].strip()
                    product_name = row['nome_produto'].strip()
                    product_category = row['categoria_produto'].strip()
                    quantity = row['quantidade'].strip()
                    total_amount = row['valor_total'].strip()

                    if not all([invoice_number, supplier_id, issue_date, product_name, product_category, quantity, total_amount]):
                        raise ValueError('Missing fields')

                    supplier = Fornecedor.objects.get(pk=supplier_id)

                    if supplier is None:
                        raise ValueError('Supplier not found')

                    try:
                        issue_date = dt.strptime(issue_date, '%Y-%m-%d')
                    except ValueError:
                        raise ValueError('issue_date format not recognized')

                    defaults = {
                        'invoice_number': invoice_number,
                        'supplier': supplier,
                        'issue_date': issue_date,
                        'product_name': product_name,
                        'product_category': product_category,
                        'quantity': quantity,
                        'total_amount': total_amount,
                    }

                    PurchaseInvoiceItems.objects.create(**defaults)

                self.stdout.write(self.style.SUCCESS('notafiscal.csv data imported'))

        except FileNotFoundError:
            self.stdout.write(
                self.style.WARNING('File not found - skipping')
            )

            return
        except Exception as e:
            self.stdout.write(
                self.style.ERROR('Error importing notafiscal.csv data')
            )

            self.stdout.write(
                self.style.ERROR(str(e))
            )

            return