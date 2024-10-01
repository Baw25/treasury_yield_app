# serializers.py

from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'term', 'amount', 'yield_rate', 'order_status', 'date_of_purchase']
