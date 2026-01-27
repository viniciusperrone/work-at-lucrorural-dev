from django_filters import rest_framework as filters

from financial.models import AccountPayable


class AccountPayableFilter(filters.FilterSet):
    deadline_start = filters.DateFilter(field_name='deadline', lookup_expr='gte')
    deadline_end = filters.DateFilter(field_name='deadline', lookup_expr='lte')
    supplier_name = filters.CharFilter(field_name='supplier__name', lookup_expr='icontains')

    class Meta:
        model = AccountPayable
        fields = ['deadline_start', 'deadline_end', 'supplier_name']
