
from django.db import models

# NOTE: TreasuryYield Model
# Date for treasury yield 
# Term fields for 1 month - 30 years
# Source of yield data
# Interest rate data type 
# Time period of data ex) 2024


class TreasuryYields(models.Model):
    date = models.DateField()  # Date of the yield
    one_mo = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    two_mo = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    three_mo = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    four_mo = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    six_mo = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    one_yr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    two_yr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    three_yr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    five_yr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    seven_yr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    ten_yr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    twenty_yr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    thirty_yr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    source = models.CharField(max_length=100)
    interest_rate_data_type = models.CharField(max_length=100)  # Type of interest rate data
    time_period = models.CharField(max_length=100)  # Time period saved by year 
    
    def __str__(self):
        return f"Treasury Yields on {self.date}"
