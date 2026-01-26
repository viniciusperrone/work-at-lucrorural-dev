from django.urls import path
from financial.views import AccountPayableCreateAPIView, AccountPayableListAPIView, AccountPayableRetrieveDestroyAPIView


urlpatterns = [
    path('financial/account-payable/create/', AccountPayableCreateAPIView.as_view(), name='financial-account-payable-create'),
    path('financial/account-payable/list/', AccountPayableListAPIView.as_view(), name='financial-account-payable-list'),
    path('financial/account-payable/<str:id>/', AccountPayableRetrieveDestroyAPIView.as_view(), name='financial-account-payable-retrieve-destroy'),
]