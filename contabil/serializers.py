from rest_framework import serializers
from rest_framework.generics import ListAPIView

from contabil.models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = '__all__'
