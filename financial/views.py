from rest_framework.generics import CreateAPIView

from financial.models import AccountPayable
from financial.serializers import AccountPayableSerializer


class CreateAccountPayableView(CreateAPIView):
    queryset = AccountPayable.objects.all()
    serializer_class = AccountPayableSerializer
