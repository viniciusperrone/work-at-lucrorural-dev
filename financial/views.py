from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveDestroyAPIView
from django.utils.translation import gettext_lazy as _

from financial.models import AccountPayable
from financial.serializers import AccountPayableSerializer


class AccountPayableListAPIView(ListAPIView):
    queryset = AccountPayable.objects.all()
    serializer_class = AccountPayableSerializer


class AccountPayableCreateAPIView(CreateAPIView):
    queryset = AccountPayable.objects.all()
    serializer_class = AccountPayableSerializer


class AccountPayableRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = AccountPayable.objects.all()
    serializer_class = AccountPayableSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def perform_destroy(self, instance):
        if instance.invoices.exists():
            raise ValidationError({
                'detail': 'Cannot delete multiple. There are linked invoices.'
            })

        instance.delete()
