from rest_framework.generics import ListAPIView

from supply.models import Supplier
from supply.serializers import SupplierSerializer


class SupplierListAPIView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
