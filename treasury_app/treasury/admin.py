from django.contrib import admin
from .models import TreasuryYields

# NOTE: Example admin app for teasury yield admin
@admin.register(TreasuryYields)
class TreasuryYieldsAdmin(admin.ModelAdmin):
    list_display = ('date', 'one_mo', 'ten_yr', 'thirty_yr', 'source', 'interest_rate_data_type')
    search_fields = ['date', 'source']