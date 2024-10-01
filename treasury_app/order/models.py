from django.db import models
from django.contrib.auth.models import User

# NOTE: Order model
# user: user or creator of order 
# term: term for treasury yield order 
# amount: amount of investment 
# yield_rate: rate at the time of purchase
# date_of_purchase: datetime 
# order_status: order status where the default is submitted
# possible statuses via a state machine: submitted, pending, approved, canceled, etc.

# models.py
from django.db import models

class Order(models.Model):
    TERM_CHOICES = [
        ('1M', '1 Month'),
        ('3M', '3 Month'),
        ('6M', '6 Month'),
        ('1Y', '1 Year'),
        ('2Y', '2 Year'),
        ('5Y', '5 Year'),
        ('10Y', '10 Year'),
        ('20Y', '20 Year'),
        ('30Y', '30 Year'),
    ]

    # Remove the user field entirely
    # NOTE: user foreign key would be here when tracking user submission
    term = models.CharField(max_length=3, choices=TERM_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    yield_rate = models.DecimalField(max_digits=5, decimal_places=2)
    date_of_purchase = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, default="submitted")

    def __str__(self):
        return f"Order for {self.amount} at {self.term}"
