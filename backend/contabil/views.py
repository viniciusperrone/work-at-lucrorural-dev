from rest_framework.generics import ListAPIView

from contabil.models import Invoice
from contabil.serializers import InvoiceSerializer


class InvoiceListView(ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
