from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import TreasuryYields
from ..serializers import TreasuryYieldsSerializer

#NOTE: View to update or delete Treasury Yields for admins
class TreasuryYieldDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TreasuryYields.objects.all()
    serializer_class = TreasuryYieldsSerializer
    lookup_field = 'date'
