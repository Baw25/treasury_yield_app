from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters import rest_framework as filters
from ..models import TreasuryYields
from ..serializers import TreasuryYieldsSerializer

# NOTE: Creating a filter for potential search queries
class TreasuryYieldFilter(filters.FilterSet):
    date = filters.DateFilter(field_name='date')
    source = filters.CharFilter(field_name='source')
    interest_rate_data_type = filters.CharFilter(field_name='interest_rate_data_type')
    term = filters.ChoiceFilter(
        method='filter_by_term',
        choices=[
            ('one_mo', '1 Month'),
            ('two_mo', '2 Month'),
            ('three_mo', '3 Month'),
            ('four_mo', '4 Month'),
            ('six_mo', '6 Month'),
            ('one_yr', '1 Year'),
            ('two_yr', '2 Year'),
            ('three_yr', '3 Year'),
            ('five_yr', '5 Year'),
            ('seven_yr', '7 Year'),
            ('ten_yr', '10 Year'),
            ('twenty_yr', '20 Year'),
            ('thirty_yr', '30 Year'),
        ]
    )

    def filter_by_term(self, queryset, name, value):
        return queryset.filter(**{value + "__isnull": False})

    class Meta:
        model = TreasuryYields
        fields = ['date', 'source', 'interest_rate_data_type', 'term']

# View to list Treasury Yields based on filters
class TreasuryYieldListView(generics.ListAPIView):
    queryset = TreasuryYields.objects.all()
    serializer_class = TreasuryYieldsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TreasuryYieldFilter
