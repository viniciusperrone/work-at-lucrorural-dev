from django.urls import path
from supply.views import SupplierListAPIView


urlpatterns = [
    path('supply/supplier/list', SupplierListAPIView.as_view(), name='supply-supplier-list'),
]