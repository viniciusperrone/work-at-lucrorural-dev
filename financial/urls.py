from django.urls import path
from financial.views import CreateAccountPayableView


urlpatterns = [
    path('financial/create/', CreateAccountPayableView.as_view(), name='financial-account-payable-create'),
]