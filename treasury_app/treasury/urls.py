from django.urls import path
from treasury.views import TreasuryYieldCreateView, TreasuryYieldListView, TreasuryYieldDetailView

urlpatterns = [
    path('create/', TreasuryYieldCreateView.as_view(), name='create_treasury_yield'),
    path('list/', TreasuryYieldListView.as_view(), name='list_treasury_yields'),
    path('<str:date>/', TreasuryYieldDetailView.as_view(), name='detail_treasury_yield'),
]