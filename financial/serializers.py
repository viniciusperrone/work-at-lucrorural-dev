from rest_framework import serializers

from financial.models import AccountPayable


class AccountPayableSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountPayable
        fields = '__all__'
        read_only_fields = ('id', 'total_amount')

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
