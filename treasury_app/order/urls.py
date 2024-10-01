from django.urls import path
from order.views import (
    OrderCreateView, 
    OrderDeleteView, 
    OrderListView, 
    OrderUpdateView, 
    OrderShowView,
)

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create_order'),
    path('list/', OrderListView.as_view(), name='list_orders'),
    path('<int:id>/', OrderShowView.as_view(), name='show_order'),
    path('<int:id>/update', OrderUpdateView.as_view(), name='update_order'),
    path('<int:id>/delete', OrderDeleteView.as_view(), name='delete_order'),
]