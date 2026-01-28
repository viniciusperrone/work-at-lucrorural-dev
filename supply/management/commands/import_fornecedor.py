import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings

from supply.models import Supplier


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'csv_file',
            type=str,
            nargs='?',
            default='supply/fixtures/fornecedor.csv',
            help='CSV file path relative to BASE_DIR'
        )

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        csv_path = os.path.join(settings.BASE_DIR, csv_file)

        try:
            with open(csv_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';')

                for row in reader:
                    supplier_id = row['id'].strip()
                    name = row['nome'].strip()
                    cnpj = row['cnpj'].strip()
                    phone = row['telefone'].strip()

                    if not all([supplier_id, name, cnpj, phone]):
                        raise ValueError('Missing fields')

                    Supplier.objects.update_or_create(
                        id=supplier_id,
                        defaults={
                            'name': name,
                            'cnpj': cnpj,
                            'phone': phone,
                        }
                    )

                self.stdout.write(self.style.SUCCESS('Supplier data imported'))

        except FileNotFoundError:
            self.stdout.write(
                self.style.WARNING('File not found - skipping')
            )

            return
        except Exception:
            self.stdout.write(
                self.style.ERROR('Error importing supplier data')
            )

            return
