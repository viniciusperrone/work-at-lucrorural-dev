from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveDestroyAPIView, UpdateAPIView
from django_filters import rest_framework as filters

from financial.models import AccountPayable
from financial.serializers import AccountPayableSerializer
from financial.filters import AccountPayableFilter


class AccountPayableListAPIView(ListAPIView):
    queryset = AccountPayable.objects.all()
    serializer_class = AccountPayableSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AccountPayableFilter


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


class AccountPayableUpdateAPIView(UpdateAPIView):
    queryset = AccountPayable.objects.all()
    serializer_class = AccountPayableSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
