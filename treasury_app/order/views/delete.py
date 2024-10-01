from rest_framework import generics, permissions
from ..models import Order
from ..serializers import OrderSerializer

class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # NOTE: Disabling for simplicity
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'