from rest_framework import serializers

from supply.models import Supplier
from utils.cnpj import format_cnpj_safe


class SupplierSerializer(serializers.ModelSerializer):
    cnpj = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'cnpj', 'phone', 'phone']


    def get_cnpj(self, obj):

        return format_cnpj_safe(obj.cnpj)

    def get_phone(self, obj):
        return Supplier.decrypt_phone(obj.phone)
