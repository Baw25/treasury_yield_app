from rest_framework import generics, status
from rest_framework.views import APIView
from ..models import TreasuryYields
from ..serializers import TreasuryYieldsSerializer

# NOTE: Sample payload
# {
#   "date": "2024-09-30",
#   "one_mo": "5.50",
#   "two_mo": "5.48",
#   "three_mo": "5.46",
#   "four_mo": "5.44",
#   "six_mo": "5.42",
#   "one_yr": "5.30",
#   "two_yr": "5.10",
#   "three_yr": "5.00",
#   "five_yr": "4.80",
#   "seven_yr": "4.60",
#   "ten_yr": "4.40",
#   "twenty_yr": "4.20",
#   "thirty_yr": "4.10",
#   "source": "US Treasury",
#   "interest_rate_data_type": "Daily Treasury Par Yield Curve Rates",
#   "time_period": "2024"
# }

# View to create a new Treasury Yield
class TreasuryYieldCreateView(generics.CreateAPIView):
    queryset = TreasuryYields.objects.all()
    serializer_class = TreasuryYieldsSerializer

