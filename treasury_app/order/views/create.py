from rest_framework import generics, permissions
from ..models import Order
from ..serializers import OrderSerializer

# NOTE: Order create payload
# {
#   "user": 1,  # user ID - for simplicity we use int instead of UUID 
#   "term": "10Y",
#   "amount": 10000.00,
#   "yield_rate": 4.5,
#   "order_status": "submitted"
# }

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # NOTE: Disabling for simplicity
    # permission_classes = [permissions.IsAuthenticated]

