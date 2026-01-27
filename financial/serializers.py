from rest_framework import serializers

from financial.models import AccountPayable
from supply.serializers import SupplierSerializer


class AccountPayableSerializer(serializers.ModelSerializer):
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = AccountPayable
        fields = ['id', 'supplier', 'deadline', 'is_paid', 'total_amount']


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['supplier'] = SupplierSerializer(instance.supplier).data

        return data


    def validate(self, data):
        supplier = data.get('supplier') or self.instance.supplier
        invoices = data.get('invoices')

        if not invoices:
            return data

        if invoices:
            invalid = [
                invoice.id
                for invoice in invoices
                if invoice.supplier_id != supplier.id
            ]

            if len(invalid) > 0:
                raise serializers.ValidationError({
                    'invoices': 'All invoices must belong to the same supplier'
                })

        return data
