from django.urls import path
from contabil.views import InvoiceListView


urlpatterns = [
    path('contabil/invoice/list', InvoiceListView.as_view(), name='contabil-invoice-list'),
]
