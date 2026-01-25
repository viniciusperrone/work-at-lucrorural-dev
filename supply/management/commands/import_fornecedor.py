import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings

from supply.models import Fornecedor


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
                    fornecedor_id = row['id'].strip()
                    nome = row['nome'].strip()
                    cnpj = row['cnpj'].strip()
                    telefone = row['telefone'].strip()

                    if not all([fornecedor_id, nome, cnpj, telefone]):
                        raise ValueError('Missing fields')

                    Fornecedor.objects.update_or_create(
                        id=fornecedor_id,
                        defaults={
                            'nome': nome,
                            'cnpj': cnpj,
                            'telefone': telefone,
                        }
                    )

                self.stdout.write(self.style.SUCCESS('Fornecedor data imported'))

        except FileNotFoundError:
            self.stdout.write(
                self.style.WARNING('File not found - skipping')
            )

            return
        except Exception as e:
            self.stdout.write(
                self.style.ERROR('Error importing fornecedor data')
            )

            return