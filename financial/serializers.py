from rest_framework import serializers

from financial.models import AccountPayable


class AccountPayableSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountPayable
        fields = '__all__'